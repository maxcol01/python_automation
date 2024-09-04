import csv

data = [
    ['Max', 'Dog', 'bacon strips', 4754],
    ['Julius', 'Cat', 'catnip', 3215],
    ['Cal', 'Cat', 'anything edible', 71142],
    ['Lena', 'Cat', 'Sheba', 142],
    ['Bruiser', 'Featherfin Catfish', 'fish pellets', 54]
]

header = ["Name", "Animal", "Food", "Costs (monthly)"]
# exactly as with text, the mode="r" will create a file if needed
# we need to create (as for reading a csv) a csv object but
# a writer one instead of a reader one !
# then we can populate it !
with open("expensive_pet.csv", mode="w") as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(header)
    csv_writer.writerows(data)
