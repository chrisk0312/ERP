from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

dataset =pd.read_csv('C:\study\ERP_chatbot\ERP\datasets\Address.csv')

@app.route('/')
def home():
    return render_template('Address.html')

@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_id = request.form['id']
        # Assuming 'Address ID' is the column name in your CSV
        result = dataset[dataset['Address ID'] == int(search_id)]
        if not result.empty:
            # Convert the result to HTML or a format that can be easily displayed
            result_html = result.to_html()
            return render_template('Address.html', result=result_html)
        else:
            return "No matching address found."
    else:
        return render_template('Address.html')


@app.route('/create/')
def create():
    return 'create'


if __name__ == '__main__':
    app.run(host='192.168.0.101', port=5000, debug=True)
    
#0331
#0330
#0327
# 03241
# 0323
# from flask import Flask, render_template, request
# from PyPDF2 import PdfFileReader
