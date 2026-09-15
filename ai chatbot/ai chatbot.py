from groq import Groq
from random import randint as ri

print("AI Chatbot")
print("Type 'exit' to quit.\n")

n = int(input("How many API keys? "))

keys = []

for i in range(n):
    keys.append(input(f"Enter key {i}: "))

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        break

    # Select a random API key
    key = keys[ri(0, len(keys) - 1)]

    # Create Groq client
    client = Groq(api_key=key)

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    ai_message = response.choices[0].message.content

    print("AI:", ai_message)