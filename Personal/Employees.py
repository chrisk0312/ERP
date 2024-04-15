import csv

def load_data(filename = "C:\\study\\ERP\\SAP_bike_sales(datasets)\\Employees.csv"):
    with open(filename, 'r', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)  # Replace this with code to insert the data into your ERP system

load_data()

#UnicodeDecodeError: 'cp949' codec can't decode byte 0xe9 in position 982: illegal multibyte sequence
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 748: invalid start byte