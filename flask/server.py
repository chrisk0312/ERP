from flask import Flask
import random 

app= Flask(__name__)

topics = [
    {'id':1, 'title':'what is ERP','body':'ERP is a type of software that connects day-to-day business processes, including inventory and order management, supply chain, accounting, human resources, and customer relationship management.'}, 
    {'id':2, 'title':'Address','body':'Address is a type of data that is used to store the address of the business.'}, 
    {'id':3, 'title':'BusinessPartners','body':'BusinessPartners is a type of data that is used to store the information of the business partners.'}, 
    {'id':4, 'title':'Employees','body':'Employees is a type of data that is used to store the information of the employees.'},
    {'id':5, 'title':'Products','body':'Products is a type of data that is used to store the information of the products.'},
    {'id':6, 'title':'Sales','body':'Sales is a type of data that is used to store the information of the sales.'} 
]

def template (contents, content):
    return f'''<!DOCTYPE html>
    <html>
        <body>
            <h1><a href="/">SAP ERP Sample</h1>
            <ol>
                {contents}
            </ol>
        </body>
    </html>'''

def getcontents ():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="{topic["id"]}/">{topic["body"]}</a></li>'
    return liTags

@app.route('/')
def index():
    return template(getcontents(), '<h2>ERP Sample</h2>Hello, SAP ERP!')
    
@app.route('/read/<int:id>/')
def read(id):
    title = ''
    body = ''
    for topic in topics:
        if topic['id'] == id:
            title = topic['title']
            body = topic['body']
            break
    return template (getcontents(), f'<h2>{title}</h2><p>{body}</p>')

@app.route('/create/')
def create():
    return 'create'


app.run(port=5001,debug=True)

#concantenate pyhton code with html code (flask)
#http://127.0.0.1:5001