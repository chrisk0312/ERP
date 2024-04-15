import csv

def load_data(filename = "C:\\study\\ERP\\SAP_bike_sales(datasets)\\Addresses.csv"):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)  # Replace this with code to insert the data into your ERP system

load_data()

#pip install nltk
#Creating a chatbot involves natural language processing

import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"who are you",
        [" IDK, How are you today ?",],
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",],
    ],
    [
        r"quit",
        ["Bye. It was nice talking to you. See you soon :)"]
    ],
]

def chatbot():
    print("Hi, I'm your chatbot. You can start a conversation with me now.")

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()