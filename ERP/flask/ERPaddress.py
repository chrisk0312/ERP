from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)

dataset =pd.read_csv('C:\study\ERP_chatbot\ERP\datasets\Address.csv')

@app.route('/')
def home():
    return render_template('Address_S.html')

@app.route('/search', methods=['POST'])
def search():
    search_id = request.form['search_id']
    # Perform the search
    result = dataset[dataset['Address ID'] == int(search_id)]
    if not result.empty:
        # Pass the search results to the template
        return render_template('Address_SR.html', tables=[result.to_html(classes='data')], titles=result.columns.values)
    else:
        return "No results found for the given Address ID."


@app.route('/create/')
def create():
    return 'create'


if __name__ == '__main__':
    app.run(host='192.168.0.101', port=5000, debug=True)

#test 0613
    
