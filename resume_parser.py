from pypdf import PdfReader

def extract_text(file):
    reader = PdfReader(file)
    text = ""
 
 
