import spacy
import re
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def extract_clauses(text):
    patterns = {
        "Termination": r"(termination.*?\\.)",
        "Liability": r"(liability.*?\\.)",
        "Confidentiality": r"(confidentiality.*?\\.)"
    }
    clauses = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text, flags=re.IGNORECASE | re.DOTALL)
        clauses[key] = matches
    return clauses

def summarize_text(text):
    return summarizer(text[:1000])[0]["summary_text"]
