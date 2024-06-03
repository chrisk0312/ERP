from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/file:///C:\\study\\ERP_chatbot\\langchain\\thesis1.pdf', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        # Get the search query from the form
        search_query = request.form.get('search')

        # Run the Python script with the search query as an argument
        result = subprocess.check_output(['python', 'test4.py', search_query])

        # Decode the output from bytes to string
        result = result.decode('utf-8')

    # Pass the output to the template
    return render_template('ERPindex.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
