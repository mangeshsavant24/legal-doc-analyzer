import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_clause_index(clauses):
    embeddings = model.encode(clauses)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return index, clauses

def find_similar_clause(query, index, clauses, top_k=3):
    q_embed = model.encode([query])
    D, I = index.search(q_embed, top_k)
    return [clauses[i] for i in I[0]]
