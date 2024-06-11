from flask import Flask, render_template, request
from PyPDF2 import PdfFileReader
from flask import request
from PyPDF2 import PdfReader
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ERPindex.html')

@app.route('/create/')
def create():
    return 'create'

from PyPDF2 import PdfReader
from flask import request


@app.route('/fetch_pdf', methods=['POST'])
def fetch_pdf():
    pdf_path = 'C:\\study\\ERP_chatbot\\ERP\\flask\\thesis1.pdf'
    search_terms = ['LangChain','prompt', 'models', 'memory', 'agents', 'stuff method']  # replace with your search terms
    try:
        with open(pdf_path, 'rb') as file:
            pdf = PdfReader(file)
            results = {}
            for page in pdf.pages:
                sentences = page.extract_text().split('.')  # split text into sentences at each period
                for sentence in sentences:
                    for term in search_terms:
                        if term in sentence and term not in results:
                            results[term] = sentence
                            break  # stop searching once a term is found
            if len(results) < len(search_terms):
                return 'Not all terms found'
            else:
                return ' '.join(results.values())
    except FileNotFoundError:
        return 'File not found'

if __name__ == '__main__':
    app.run(host='192.168.0.101', port=5000, debug=True)
    
#0611
# from flask import Flask, render_template, request
# from PyPDF2 import PdfFileReader