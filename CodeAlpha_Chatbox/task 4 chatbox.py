print("=== BASIC CHATBOT ===")
print("Type 'bye' to exit.")
print()

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi" or user == "hey":
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine, thank you!")

    elif user == "what is your name" or user == "who are you":
        print("Bot: I am a simple chatbot.")

    elif user == "bye" or user == "goodbye" or user == "exit":
        print("Bot: Goodbye! Have a nice day!")
        break

    elif user == "help":
        print("Bot: I can say hello, tell my name, or say goodbye.")

    elif "python" in user:
        print("Bot: Python is a great programming language!")

    elif "time" in user:
        import datetime
        now = datetime.datetime.now()
        print("Bot: Current time is", now.strftime("%I:%M %p"))

    elif "date" in user:
        import datetime
        today = datetime.datetime.now()
        print("Bot: Today is", today.strftime("%B %d, %Y"))

    elif "thank" in user:
        print("Bot: You are welcome!")

    else:
        print("Bot: I don't understand that. Try 'help'.")