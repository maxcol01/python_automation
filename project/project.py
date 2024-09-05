from datetime import datetime
import csv

mapping = {"P001": ["Wireless Headphones", 100],
           "P002": ["Laptop Backpack", 60],
           "P003": ["Bluetooth Speaker", 50],
           "P004": ["USB flash Drive", 20],
           "P005": ["Mobile Phone Case", 15],
           "P006": ["Wireless Mouse", 30],
           "P007": ["Laptop Stand", 40],
           "P008": ["HDMI Cable", 15],
           "P009": ["Smartphone", 600],
           "P010": ["External Hard Drive", 100]
           }

header = ["Current Date", "Sale ID", "Product ID", "Name", "Price"]
formatted_data = list()
with open("product_sales.txt", mode="r") as raw_file:
    content = raw_file.readlines()
    counter = 0
    for row in content:
        counter += 1
        # remove the \n from the .readlines()
        row = row.strip()
        # format all the information within a list
        list_data = [datetime.now().strftime("%Y-%M-%D"), counter, row, mapping[row][0], mapping[row][1]]
        formatted_data.append(list_data)

print(formatted_data)