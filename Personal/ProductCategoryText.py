import csv

def load_data(filename = "C:\\study\\ERP\\SAP_bike_sales(datasets)\\ProductCategoryText.csv"):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)  # Replace this with code to insert the data into your ERP system

load_data()