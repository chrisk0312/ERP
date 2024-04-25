from flask import Flask, render_template, request
from langchain import LangChain

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
    user_input = request.args.get('msg')
    return lc.get_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
