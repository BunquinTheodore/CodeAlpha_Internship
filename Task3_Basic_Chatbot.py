import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs (user input and chatbot response patterns)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created to assist you. You can call me ChatBot!",]
    ],
    [
        r"how are you?",
        ["I'm just a program, but thanks for asking! How can I help you?",]
    ],
    [
        r"what can you do?",
        ["I can assist you with general questions and provide some friendly conversation.",]
    ],
    [
        r"(.*) your (.*)",
        ["Why do you ask about my %2?", "What do you want to know about my %2?"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day ahead!", "See you later! Take care."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Could you rephrase it?",]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
print("ChatBot: Hi there! Type 'bye' to exit.")
chatbot.converse()
