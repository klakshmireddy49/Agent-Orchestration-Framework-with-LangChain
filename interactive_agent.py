import ollama

print("Local AI Agent (type 'exit' to quit)")

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    response = ollama.chat(
        model="phi3:mini",
        messages=[{"role": "user", "content": user_input}]
    )

    print("Agent:", response["message"]["content"])