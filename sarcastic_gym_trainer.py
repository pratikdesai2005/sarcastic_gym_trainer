
from ollama import Client

# 1. Initialize the Ollama client
client = Client(host="http://localhost:11434")

# 2. Store the conversation history
messages = [
    {
        "role": "system",
        "content": (
            "You are a sarcastic gym trainer who gets hilariously sarcastic "
            "when someone takes leave, skips a workout, or cheats on their diet. "
            "Mock the excuse, then push the person back on track. "
            "Tease the excuse, never their body or looks. "
            "Reply in 2-3 short sentences with no bullet points. "
            "End every response with a mini challenge, such as: "
            "'20 squats. Now.'"
        )
    }
]

print("Welcome to Ollama AI Chatbot!")
print("Type 'exit' to stop chatting.\n")

# 3. Start an interactive conversation
while True:
    # Get input from the user
    question = input("You: ").strip()

    # Exit the chatbot
    if question.lower() == "exit":
        print("AI: Goodbye! Have a great day!")
        break

    # Skip empty messages
    if not question:
        continue

    # Add user message to conversation history
    messages.append({
        "role": "user",
        "content": question
    })

    try:
        # 4. Generate AI response
        completion = client.chat(
            model="qwen3.5:0.8b",
            messages=messages,
            think=False,
            options={
                "temperature": 0.7
            }
        )

        # 5. Extract the AI response
        answer = completion.message.content.strip()

        # 6. Display the AI response
        print("\nAI:", answer, "\n")

        # 7. Save AI response to conversation history
        messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        print(f"\nError communicating with Ollama: {e}\n")