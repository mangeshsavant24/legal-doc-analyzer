import streamlit as st
from utils.parser import extract_text
from utils.nlp_engine import extract_entities, extract_clauses, summarize_text
from utils.scorer import score_document
from utils.faiss_index import build_clause_index, find_similar_clause
from utils.gpt_helper import explain_in_simple_terms, ask_gpt_chat
from components.signer import sign_ui
from components.voice import speak

st.set_page_config(page_title="Legal Document Analyzer", layout="wide")
st.title("📄 Legal Document Analyzer")
st.markdown("Analyze legal PDFs/DOCX/TXT, extract clauses, and ask GPT for plain-English explanations.")

st.sidebar.header("📂 Upload Legal Documents")
uploaded_files = st.sidebar.file_uploader("Choose documents", type=["pdf", "docx", "txt"], accept_multiple_files=True)

if uploaded_files:
    docs_data = []

    for uploaded in uploaded_files:
        ext = uploaded.name.split('.')[-1]
        with st.spinner(f"Processing {uploaded.name}..."):
            text = extract_text(uploaded, ext)
            entities = extract_entities(text)
            clauses = extract_clauses(text)
            summary = summarize_text(text)
            score, recs = score_document(clauses)

            docs_data.append({
                "filename": uploaded.name,
                "text": text,
                "entities": entities,
                "clauses": clauses,
                "summary": summary,
                "score": score,
                "recommendations": recs
            })

    for doc in docs_data:
        st.subheader(f"📄 {doc['filename']}")
        st.write("### 📌 Summary")
        st.success(doc["summary"])

        st.write("### 🏷️ Entities")
        st.info(", ".join(doc["entities"]))

        st.write("### 📑 Clauses")
        for i, clause in enumerate(doc["clauses"]):
            with st.expander(f"Clause {i+1}"):
                st.write(clause)
                if st.button(f"Explain Clause {i+1}", key=f"explain-{i}"):
                    explanation = explain_in_simple_terms(clause)
                    st.markdown(f"**🧠 Explained:** {explanation}")
                    speak(explanation)

        st.write("### ✅ Risk & Recommendation")
        sign_ui(doc["score"], doc["recommendations"])

    st.divider()

    st.header("🔍 Compare Clause Similarity")
    all_clauses = sum([doc["clauses"] for doc in docs_data], [])
    clause_query = st.text_area("Enter a clause to compare:", height=100)
    if st.button("🔎 Find Most Similar"):
        index, base = build_clause_index(all_clauses)
        similar = find_similar_clause(clause_query, index, base)
        st.code(similar)

    st.divider()

    st.header("💬 Ask a Legal Question (GPT-4)")
    context = st.text_area("Optional context (e.g. clause or contract):", height=150)
    question = st.text_input("Ask a question:")
    if st.button("🤖 Ask GPT"):
        reply = ask_gpt_chat(question, context)
        st.markdown(f"**GPT-4 Answer:** {reply}")
        speak(reply)
