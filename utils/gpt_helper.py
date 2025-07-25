import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your key or use env variable

def explain_in_simple_terms(text):
    prompt = f"Explain this legal clause in simple layman's terms:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response['choices'][0]['message']['content'].strip()
