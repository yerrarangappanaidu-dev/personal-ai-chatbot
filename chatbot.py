
import ollama


def get_ai_response(messages):
    response = ollama.chat(
        model="gemma3:1b",
        messages=messages
    )

    return response["message"]


def start_chatbot():
    print("================================")
    print("   PERSONAL AI CHATBOT")
    print("================================")
    print("I can remember this conversation.")
    print("Type 'exit' to quit.")

    messages = []

    while True:
        user_message = input("\nYou: ").strip()

        if user_message.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        if not user_message:
            print("Chatbot: Please enter a message.")
            continue

        messages.append({
            "role": "user",
            "content": user_message
        })

        try:
            response_message = get_ai_response(messages)

            messages.append(response_message)

            print("\nChatbot:", response_message["content"])

        except Exception as error:
            print("\nChatbot error:", error)


if __name__ == "__main__":
    start_chatbot()