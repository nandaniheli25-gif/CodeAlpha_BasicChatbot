def chatbot(user_input):

    user_input = user_input.lower()

    if user_input == "hello":
        return "Hello!"

    elif user_input == "how are you":
        return "I'm fine, thanks for asking."

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "":
        return "Please type something."

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."

print("----- Welcome to the Basic Chatbot -----")

user_name = input("Enter your name: ")

print("Welcome", user_name , "!")
print("You can start chatting with the bot.")
print("Type 'bye' anytime to stop the chat.")

while True:

    message = input("You: ")
    response = chatbot(message)
    print("Bot:", response)

    if message.lower() == "bye":
        break

print("Chat ended successfully.")


