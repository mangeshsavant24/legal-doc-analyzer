import openai

def ask_gpt_chat(question, context):
    prompt = f"Document context:\n{context}\n\nUser question: {question}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content'].strip()
