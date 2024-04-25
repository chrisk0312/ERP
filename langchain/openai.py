from flask import Flask, render_template, request

app = Flask(__name__)

def get_chatbot_response(user_input):
    user_input = user_input.lower()
    if 'hello' in user_input:
        return "Hello! How can I help you today?"
    elif 'goodbye' in user_input:
        return "Goodbye! Have a great day!"
    elif 'order' in user_input:
        return "Sure, let me help you with that. Please provide me with the details of your order."
    elif 'invoice' in user_input:
        return "Of course, could you please provide me with the invoice number?"
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    return get_chatbot_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
