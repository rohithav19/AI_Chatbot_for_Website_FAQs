import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["***WELCOME TO ROHITHA UNIVERSITY***"
         "Hi! How can I assist you?"]
    ],
   
    [
        r"want to know the fees?",
        ["Provide your branch",]
    ],
    [
        r"CSE",
        [
        " Tution fee: 40000"
        "   Miscellanous fees: 30000"]
    ],
    [
        r"AI/ML|EEE",
        [
        " Tution fee: 40000"
        "   Miscellanous fees: 20000"]
    ],
    [
        r"ECE",
        [
        " Tution fee: 40000"
        "   Miscellanous fees: 40000"]
    ],
    
    [
        r"bba|bca|bcom|degree",
        ["For any degree:"
        " Tution fee: 20000"
        "   Miscellanous fees: 20000"]
    ],
    [
        r"MBA|MCA",
        ["For Masters:"
        " Tution fee: 80000"
        "   Miscellanous fees: 200000"]
    ],
    [
        r"help| assist",
        ["Sure, I'd be happy to help. What do you need assistance with?"]
    ],
    [
        r"which course is better?",
        ["Currently most popular course is CSE"]
    ],
    [
        r"bye|goodbye",
        [ "Bye, take care!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that Could you try saying that again?"]
    ]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def chat():
    print("Hi! I'm Ro, your virtual assistant. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Ro:", response)
        if user_input.lower() == 'bye':
            break

if __name__ == "__main__":
    chat()