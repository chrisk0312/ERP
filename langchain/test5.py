from flask import Flask, render_template, request
from langchain import LangChain
from PyPDF2 import PdfReader
import os
import pickle

app = Flask(__name__)

# Initialize LangChain
lc = LangChain()

# Define your language chain
lc.add_chain([
    {
        "input": "hello",
        "output": "Hello! How can I help you today?"
    },
    {
        "input": "goodbye",
        "output": "Goodbye! Have a great day!"
    },
    {
        "input": "order",
        "output": "Sure, let me help you with that. Please provide me with the details of your order."
    },
    {
        "input": "invoice",
        "output": "Of course, could you please provide me with the invoice number?"
    },
    {
        "input": "default",
        "output": "I'm sorry, I didn't understand that. Could you please rephrase?"
    }
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    langchain = importlib.import_module('langchain')
    lc = langchain.LangChain()
    user_input = request.args.get('msg')
    return lc.get_response(user_input)

def process_pdf(pdf_path):
    # Load PDF
    pdf = PdfReader(pdf_path)
    
    # Split, embed, and store text content of each page
    embedded_texts = []
    for page in pdf.pages:
        text = page.extract_text()
        embedded_texts.append(text)
    
    # Store embedded text content
    with open('embedded_texts.pkl', 'wb') as f:
        pickle.dump(embedded_texts, f)
    
    # Retrieve embedded text content when asked a question
    def chatbot(question):
        with open('embedded_texts.pkl', 'rb') as f:
            embedded_texts = pickle.load(f)
        for text in embedded_texts:
            if question in text:
                return text
        return "Sorry, I couldn't find any information related to your question."
    
    return chatbot

    
# Example usage
if __name__ == "__main__":
    pdf_path = "C:\\study\\ERP_chatbot\\thesis1.pdf"
    chatbot = process_pdf(pdf_path)
    
    # Test the chatbot
    question = input("Ask a question about the PDF: ")
    answer = chatbot(question)
    print(answer)

    app.run(debug=True)