
def start_chatbot():
    print("Welcome to My Personal AI Chatbot!")
    print("Type 'exit' to stop.")

    while True:
        user_message = input("\nYou: ")

        if user_message.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        print("You typed:", user_message)


start_chatbot()
