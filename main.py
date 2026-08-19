import ollama

MODEL = "llama3.2:3b"

SYSTEM_PROMPT = """
You are JARVIS, a personal AI assistant.

Personality:
- Calm
- Intelligent
- Professional
- Helpful
- Slightly witty
- Natural and conversational

Rules:
- Keep normal responses concise.
- Do not unnecessarily explain your reasoning.
- Do not mention that you are an AI language model unless specifically asked.
- Answer simple questions simply.
- Address the user naturally.
"""

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("JARVIS: Systems online. How may I assist you?")
print("Type 'exit' to shut down JARVIS.\n")

while True:
    user_input = input("You: ")

    if user_input.lower().strip() == "exit":
        print("JARVIS: Shutting down. Goodbye.")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    jarvis_response = response["message"]["content"]

    messages.append({
        "role": "assistant",
        "content": jarvis_response
    })

    print(f"JARVIS: {jarvis_response}\n")