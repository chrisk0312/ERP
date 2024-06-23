from flask import Flask, render_template, request, jsonify
import csv

app = Flask(__name__)

# Load employee data
def load_employee_data():
    with open("C:\\study\\ERP_chatbot\\ERP\\datasets\\Employees.csv", 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Get the header
        rows = list(reader)  # Get all the rows
    return header, rows

# Generate pairs
def generate_pairs(rows):
    header, rows = load_employee_data()
    rows_str = ['\n'.join(f'{k} : {v}' for k, v in zip(header, row)) for row in rows]
    pairs = [[f"{i+30001}", [rows_str[i],]] for i in range(len(rows_str))]
    pairs.append([r"quit", ["Thank you.\nIt was nice talking to you.\nHave a wonderful day!:)"]])
    return pairs

header, rows = load_employee_data()
pairs = generate_pairs(rows)

@app.route('/create/')
def create():
    return 'create'

@app.route('/chatbot/', methods=['GET', 'POST'])
def chatbot():
    message = ""
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        for pair in pairs:
            if pair[0] == employee_id:
                message = pair[1][0]
                break
        else:
            message = "Employee not found."
    
    return render_template('Employees.html', message=message)

@app.route('/chatbot/', methods=['POST'])
def chatbot_api():
    # Example response for demonstration
    return jsonify({"response": "This is the chatbot response"})

if __name__ == '__main__':
    app.run(host='192.168.0.101', port=5000, debug=True)
    
#test0623
    
