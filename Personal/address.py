# ref = https://www.sap.com/korea/about/company/office-locations.html

import csv
from nltk.chat.util import Chat, reflections

# Read the CSV file and store all the rows
with open("C:\\study\\ERP\\SAP_bike_sales(datasets)\\Addresses.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get the header
    rows = list(reader)  # Get all the rows

# Combine the header and each row into a dictionary, then convert to a string
rows_str = ['\n'.join(f'{k.replace("癤풞", "A")} : {v}' for k, v in zip(header, row)) for row in rows]

# Generate pairs using a loop
pairs = [[f"{i+10001}", [rows_str[i],]] for i in range(len(rows_str))]

pairs.append([r"quit", ["Thank you.\nIt was nice talking to you. \nHave a wonderful day!:)"]])

def chatbot():
    print("Hello!\nI am here to help you find SAP Asia Pacific region office.\n"
          "Please enter the Address ID you wish to search for.\n"
          "Address ID is a 5 digit number starting from 10001 to 10045."
          )

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
    

'''

import csv
from nltk.chat.util import Chat, reflections

# Read the CSV file and store all the rows
with open("C:\\study\\ERP\\SAP_bike_sales(datasets)\\Addresses.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Get the header
    rows = list(reader)  # Get all the rows

# # Combine the header and each row into a dictionary, then convert to a string
# rows_str = ['\n'.join(f'{k} : {v}' for k, v in zip(header, row)) for row in rows]

# Combine the header and each row into a dictionary, then convert to a string
rows_str = ['\n'.join(f'{k.replace("癤풞", "A")} : {v}' for k, v in zip(header, row)) for row in rows]

pairs = [
    [
        r"10001",
        [rows_str[0],],
    ],
    [
        r"10002",
        [rows_str[1],],
    ],
    [
        r"10003",
        [rows_str[2],], 
    ],
    [
        r"10004",
        [rows_str[3],], 
    ],
        [
        r"10005",
        [rows_str[4],],
    ],
    [
        r"10006",
        [rows_str[5],],
    ],
    [
        r"10007",
        [rows_str[6],], 
    ],
    [
        r"10008",
        [rows_str[7],], 
    ],
    [
        r"10009",
        [rows_str[8],],
    ],
    [
        r"10010",
        [rows_str[9],],
    ],
    [
        r"10011",
        [rows_str[10],], 
    ],
    [
        r"10012",
        [rows_str[11],], 
    ],
        [
        r"10013",
        [rows_str[12],],
    ],
    [
        r"10014",
        [rows_str[13],],
    ],
    [
        r"10015",
        [rows_str[14],], 
    ],
    [
        r"10016",
        [rows_str[15],], 
    ],
    [
        r"10017",
        [rows_str[16],],
    ],
    [
        r"10018",
        [rows_str[17],],
    ],
    [
        r"10019",
        [rows_str[18],], 
    ],
    [
        r"10020",
        [rows_str[19],], 
    ],
        [
        r"10021",
        [rows_str[20],],
    ],
    [
        r"10022",
        [rows_str[21],],
    ],
    [
        r"10023",
        [rows_str[22],], 
    ],
    [
        r"10024",
        [rows_str[23],], 
    ],
    [
        r"10025",
        [rows_str[24],],
    ],
    [
        r"10026",
        [rows_str[25],],
    ],
    [
        r"10027",
        [rows_str[26],], 
    ],
    [
        r"10028",
        [rows_str[27],], 
    ],
    [
        r"10029",
        [rows_str[28],],
    ],
    [
        r"10030",
        [rows_str[29],],
    ],
    [
        r"10031",
        [rows_str[30],], 
    ],
    [
        r"10032",
        [rows_str[31],], 
    ],
    [
        r"10033",
        [rows_str[32],],
    ],
    [
        r"10034",
        [rows_str[33],],
    ],
    [
        r"10035",
        [rows_str[34],], 
    ],
    [
        r"10036",
        [rows_str[35],], 
    ],
    [
        r"10037",
        [rows_str[36],],
    ],
    [
        r"10038",
        [rows_str[37],],
    ],
    [
        r"10039",
        [rows_str[38],], 
    ],
    [
        r"10040",
        [rows_str[39],], 
    ],
     [
        r"10041",
        [rows_str[40],],
    ],
    [
        r"10042",
        [rows_str[41],],
    ],
    [
        r"10043",
        [rows_str[42],], 
    ],
    [
        r"10044",
        [rows_str[43],], 
    ],
        [
        r"10045",
        [rows_str[44],],
    ],
    
]

def chatbot():
    print("Hello, Please type Address ID.")

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
'''
    
