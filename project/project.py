from datetime import datetime
import csv


#  Prepare the data
def prepare_data(fd: list, mapp: dict, file_path_to) -> list:
    with open(file_path_to, mode="r") as raw_file:
        content = raw_file.readlines()
        counter = 0
        for row in content:
            counter += 1
            # remove the \n from the .readlines()
            row = row.strip()
            # format all the information within a list
            list_data = [datetime.now().strftime("%Y-%M-%D"), counter, row, mapp[row][0], mapp[row][1]]
            fd.append(list_data)
    return fd


#  Create the CSV file
def create_csv(hd: list, fd: list) -> None:
    with open("sale_today.csv", mode="w") as new_file:
        data_info = csv.writer(new_file)
        data_info.writerow(hd)
        data_info.writerows(fd)


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
file_path = "product_sales.txt"


create_csv(hd=header, fd=prepare_data(fd=formatted_data, mapp=mapping, file_path_to=file_path))
