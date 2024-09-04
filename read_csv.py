import csv

with open("toy_data.csv", mode="r") as file:
    # access the information inside a .csv file
    content = csv.reader(file)
    # skip the header
    next(content)
    # loop over the row of the csv (return a list of each element within a column
    for row in content:
        print(row)

