from chatgpt import ChatGPT

chatbot = ChatGPT()
while True:
    text = input("You: ")
    response = chatbot.generate_response(text)

    print("Chatbot:", response)
