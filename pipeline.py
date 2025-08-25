# Pipeline backend for refactoring code
import fitz
import spacy
import re
import pandas as pd
from sentence_transformers import SentenceTransformer
import streamlit as st

#creating an object for Spacy Sentencizer
nlp = spacy.blank('en')
nlp.add_pipe('sentencizer')

@st.cache_resource
def load_embed():
    return SentenceTransformer(model_name_or_path="all-mpnet-base-v2")

embed_model = load_embed()

# a pretty printer
def format_text(text_in: str)->str:
    return text_in.replace("\n", " ").strip()

# Function for reading pdf using pymupdf
def read_pdf(path)->list[dict]:
    if isinstance(path, str):
        doc = fitz.open(path)
    else:
        doc = fitz.open(stream=path.read(), filetype="pdf")
    
    content_dict = []
    for page, content in enumerate(doc):
        text = content.get_text()
        text = format_text(text_in=text)
        doc_nlp = nlp(text)
        sentences = [sent.text.strip() for sent in doc_nlp.sents]
        content_dict.append({"page_number":page, 
                             "page_text": text, 
                             "text_length": len(text), 
                             "word_count": len(text.split(" ")),
                             "sentences": sentences,
                             "sentence_count": len(sentences)
                             })

    return content_dict

def create_chunks(string_input: list[dict])->list[dict]:
    for itmz in string_input:
        itmz["text_chunk"]=convert_sentences_to_chunk(input=itmz["sentences"], split_size=10)
        itmz["text_chunk_size"]=len(itmz["text_chunk"])
    
    return string_input

def convert_sentences_to_chunk(input: list[str], split_size: int = 10)->list[list[str]]:
    '''This function will essentially convert sentences into sentence chunks of size 10 or less, and will return a list containing a list of string'''
    return [input[i:i+split_size] for i in range(0, len(input), split_size)]

def convert_chunks_for_embed(input_text_info: list[dict])->list[dict]:
    '''Splitting Chunks for ease of embeddings'''
    split_chunk = []
    for items in input_text_info:
        for parts in items["text_chunk"]:
            chunk_store = {}
            chunk_store["pg_no"]=items["page_number"]

            join_sentences_chunks = " ".join(parts).strip()
            join_sentences_chunks = re.sub(r'\.([A-Z])', r'. \1', join_sentences_chunks)

            chunk_store["chunk_store"]=join_sentences_chunks
            chunk_store["chunk_store_size"]=len(join_sentences_chunks)
            chunk_store["chunk_store_word_count"]=len(join_sentences_chunks.split()) # word count
            chunk_store["chunk_store_token_count"]=len(join_sentences_chunks.split())/4

            split_chunk.append(chunk_store)

    return split_chunk
     
def filter_token_count(input_chunk_test: list[dict], min_token_count: int = 15):
    int_chunk_text = pd.DataFrame(input_chunk_test)
    filtered_text = int_chunk_text[int_chunk_text["chunk_store_token_count"]>min_token_count]
    return filtered_text.to_dict(orient="records")
    

def convert_text_to_embeddings(input_store: list[dict]):
    '''To convert text into embeddings'''
    for items in input_store:
        items["embeddings"]=embed_model.encode(items["chunk_store"])
    
    return input_store