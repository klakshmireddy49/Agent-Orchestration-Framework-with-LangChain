import ollama
response = ollama.chat(
    model="phi3:mini",
    messages=[
        {"role": "user", "content": "Explain artificial intelligence"}
    ]
)

print(response["message"]["content"])