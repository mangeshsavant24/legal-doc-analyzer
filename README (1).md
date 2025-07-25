# 📄 Legal Document Analyzer

This AI-powered web app helps you quickly understand, assess, and compare legal documents. Upload PDF, DOCX, or TXT files, and the app will extract entities, key clauses (like termination or liability), generate a summary, and evaluate risk.

Built with Python, Streamlit, and OpenAI GPT-4 — ideal for students, startups, or anyone needing legal clarity without legal fees.

---

## 🚀 Features

- 📤 Upload multiple legal files (PDF, DOCX, TXT)
- 🔍 Extract legal clauses, entities, and summaries
- ✅ Auto-score contract risk and offer sign/reject suggestion
- 🤖 Ask GPT-4 to explain terms in plain English
- 🔊 Voice support to hear explanations aloud
- 📚 Compare similar clauses with FAISS search

---

## 🧠 Tech Stack

- Python, Streamlit
- spaCy, Transformers, Sentence Transformers
- FAISS for clause similarity
- OpenAI GPT-4 API

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/legal-doc-analyzer.git
cd legal-doc-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up OpenAI API Key

You can either:

- Create a `.env` file:

```env
OPENAI_API_KEY=your-key-here
```

- Or use Streamlit Cloud Secrets.

### 4. Run the App Locally

```bash
streamlit run app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

1. Push this repo to GitHub
2. Go to https://streamlit.io/cloud
3. Deploy the app, selecting `app.py` as the main file
4. Set your OpenAI API key in **Secrets**

---

## 📁 Project Structure

```
.
├── app.py
├── requirements.txt
├── Procfile
├── README.md
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

## ✨ License

MIT License

---

Made with ❤️ for accessible legal insights.