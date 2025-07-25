import spacy
from transformers import pipeline

# Ensure model is downloaded
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

summarizer = pipeline("summarization")

def extract_entities(text):
    doc = nlp(text)
    return [f"{ent.text} ({ent.label_})" for ent in doc.ents]

def extract_clauses(text):
    return [s.text.strip() for s in nlp(text).sents if len(s.text.strip()) > 50]

def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summary = " ".join([summarizer(c, max_length=100, min_length=30, do_sample=False)[0]['summary_text'] for c in chunks])
    return summary
