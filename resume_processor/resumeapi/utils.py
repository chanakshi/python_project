import re
from docx import Document
from PyPDF2 import PdfReader

def extract_from_docx(file):
    doc = Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return extract_details(text)

def extract_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return extract_details(text)

def extract_details(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+?\d[\d -]{8,12}\d'

    email = re.findall(email_pattern, text)
    phone = re.findall(phone_pattern, text)

    name = text.split()[0] if text else "Unknown"
