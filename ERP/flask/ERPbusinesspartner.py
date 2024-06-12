from flask import Flask, render_template, request
from PyPDF2 import PdfFileReader
from flask import request
from PyPDF2 import PdfReader
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('BusinessPartners.html')

@app.route('/create/')
def create():
    return 'create'


if __name__ == '__main__':
    app.run(host='192.168.0.101', port=5000, debug=True)
    
#0611
# from flask import Flask, render_template, request
# from PyPDF2 import PdfFileReader