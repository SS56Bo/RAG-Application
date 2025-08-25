import streamlit as st
from pipeline import read_pdf, create_chunks, convert_chunks_for_embed, filter_token_count, convert_text_to_embeddings
st.title("📄 RAG Chatbot")
st.markdown(
    """
    Upload your PDF and let our **Retrieval-Augmented Generation (RAG)** model  
    build an intelligent chatbot that can answer your questions directly from the document.  

    🔹 No more scrolling through pages  
    🔹 Just ask, and get answers in seconds  
    """
)

store_pdf = st.file_uploader("Upload PDF", type="pdf")

if store_pdf is not None:
    pdf_content = read_pdf(store_pdf)
    chunk_content = create_chunks(pdf_content)
    split_chunks = convert_chunks_for_embed(chunk_content)
    filtered_split_texts = filter_token_count(split_chunks)
    embed_text = convert_text_to_embeddings(filtered_split_texts)
    st.write(embed_text[0])