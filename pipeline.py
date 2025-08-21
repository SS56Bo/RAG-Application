# Pipeline backend for refactoring code
import os
import fitz

# Function for reading pdf using pymupdf
def read_pdf(path:str):
    #make a check if the filetype is pdf or not
    doc = fitz.open(path)
    return doc


