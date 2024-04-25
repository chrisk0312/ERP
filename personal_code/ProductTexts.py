# ref = https://www.sap.com/products/erp.html 
import csv
from nltk.chat.util import Chat, reflections

with open("C:\\study\\ERP\\SAP_bike_sales(datasets)\\ProductTexts.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get the header
    rows = list(reader)  # Get all the rows

# Combine the header and each row into a dictionary, then convert to a string
rows_str = ['\n'.join(f'{k} : {v}' for k, v in zip(header, row)) for row in rows]

# Generate pairs using a loop
pairs = [[f"{i+40001}", [rows_str[i],]] for i in range(len(rows_str))]

pairs.append([r"quit", ["Thank you.\nIt was nice talking to you.\nHave a wonderful day!:)"]])

def chatbot():
    print("Hello!\nI am here to help you find sample of SAP ProductTexts.\n"
          "Please enter the ProductText category ID you wish to search for.\n"
          "ProductText category ID is a 5 digit number starting from 40001 to 40009."
          )

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()

