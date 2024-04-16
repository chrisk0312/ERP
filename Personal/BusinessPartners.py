# ref = https://www.sap.com/partners/find.html#active_tab_item_1666104644409

import csv
from nltk.chat.util import Chat, reflections

with open("C:\\study\\ERP\\SAP_bike_sales(datasets)\\BusinessPartners.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get the header
    rows = list(reader)  # Get all the rows

# Combine the header and each row into a dictionary, then convert to a string
rows_str = ['\n'.join(f'{k} : {v}' for k, v in zip(header, row)) for row in rows]

# Generate pairs using a loop
pairs = [[f"{i+20001}", [rows_str[i],]] for i in range(len(rows_str))]

pairs.append([r"quit", ["Thank you.\nIt was nice talking to you. \nHave a wonderful day!:)"]])

def chatbot():
    print("Hello!\nI am here to help you find which company is SAP global strategic partners.\n"
          "Please enter the PartnerID you wish to search for.\n"
          "Address ID is a 5 digit number starting from 20001 to 20060."
          )

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()