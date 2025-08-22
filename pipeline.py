# Pipeline backend for refactoring code
import fitz
import spacy.lang.en as English

#creating an object of English
eng = English()
eng.add_pipe("sentencizer")

# Function for reading pdf using pymupdf
def read_pdf(path:str)->list[str]:
    doc = fitz.open(path)
    content_dict = []
    for page, content in enumerate(doc):
        text = content.get_text()
        text = format_text(text_in=text)
        content_dict.append({"page_number":page, "page_text": text, "text_length": len(text), "word_count": len(text.split(" "))})
        # adding sentencizer to create one document at a time

    return content_dict

def format_text(text_in: str)->str:
    return text_in.replace("\n", " ").strip()

# conversion into sentences
def split_into_sentences(list_obj: list[str])->list[str]:
    for items in list_obj:
        items["sentence"]=list(eng(items["text"]).sents)
        items["sentences"]= [str(sentence) for sentence in items["sentences"]]
        items["sentences_count_spacy"] = len(items["sentences"])
    return items

