import pdfplumber
import docx

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file, filetype):
    if filetype == "pdf":
        return extract_text_from_pdf(file)
    elif filetype == "docx":
        return extract_text_from_docx(file)
    elif filetype == "txt":
        return file.read().decode("utf-8")
    return ""
