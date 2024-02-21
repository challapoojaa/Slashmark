import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you.",]
    ],
    [
        r"sorry (.*)",
        ["No problem, please continue.",]
    ],
    [
        r"quit",
        ["Goodbye, have a great day!",]
    ],
    [
        r"what can you do",
        ["I can provide information, answer questions, and chat with you.",]
    ],
    [
        r"how old are you",
        ["I don't have an age, as I am a computer program.",]
    ],
    [
        r"where are you from",
        ["I exist in the digital world, so I don't have a physical location.",]
    ],
    [
        r"tell me a joke",
        ["Why couldn’t the bicycle stand up by itself? It was two tired!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand. Can you please rephrase your question?",]
    ],
]

def chatbot():
    print("Hi, I'm Chatbot! How can I assist you today?")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()
