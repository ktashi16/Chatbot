#  Natural language Toolkit
# Chat is a class that provides logic for building the chatbot
# Reflections contains a set of input text and its corresponding output values.
import nltk
from nltk.chat.util import Chat, reflections

# Creating rules that will be used to train the chatbot.
# The first element is the user input
# Second element is the response from the bot.
set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you?","Hi %1, Welcome",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?|Who are you?",
        ["I am Chatbot. Ask me a math question, please",]
    ],
    [
        r"show me the pythagorean theorem",
        ["a squared plus b squared equals c squared",]
    ],
    [
        r"do you know the law of cosines?",
        ["c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)",]
    ],

    [
        r"Thank you|thanks",
        ["I am happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

# Defining chatbot and it prints whenever the function is invoked.
def chatbot():
    print("Welcome")
chatbot()

# Instantiate the Chat() function containing the set_pairs and reflections
chat = Chat(set_pairs, reflections)


# Instantiate the conversation with converse() function which triggers the conversation.
chat.converse()

if __name__ == "__main__":
    chatbot()
