# 📄 Legal Document Analyzer (Streamlit App)

This is an NLP-powered Streamlit web app that lets you analyze legal documents in PDF, DOCX, or TXT format. It can extract key clauses, entities, generate summaries, check risks, and explain terms in simple language using GPT-4.

## 🚀 Features
- 📤 Upload multiple documents (PDF, DOCX, TXT)
- 📑 Extract key clauses, legal entities, and summaries
- ✅ Risk scoring and signing recommendation
- 🔍 Compare clause similarity using FAISS
- 🤖 Ask GPT-4 legal questions with voice playback

## 🧠 Tech Stack
- Python, Streamlit
- spaCy, HuggingFace Transformers, SentenceTransformers
- FAISS for similarity search
- OpenAI GPT-4 for clause explanation and chat

## 🔧 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/legal-doc-analyzer.git
   cd legal-doc-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your-key-here" > .env
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## 📦 Deployment

This app is ready for Streamlit Cloud deployment. Add your `OPENAI_API_KEY` in the secret manager.

## 📁 Project Structure

```
├── app.py
├── requirements.txt
├── Procfile
├── .streamlit/
│   └── config.toml
├── utils/
│   ├── parser.py
│   ├── nlp_engine.py
│   ├── scorer.py
│   ├── faiss_index.py
│   └── gpt_helper.py
└── components/
    ├── signer.py
    ├── chatbot.py
    └── voice.py
```

---
Made with ❤️ for legal clarity.
