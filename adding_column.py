import csv


# Instruction
# add a column to the csv file called "rating category"
#  if <= -3 - abysmal
#  if <= -1 - awful
#  else - bad

# function for rating
def rating_category(rat: int) -> str:
    """
    categorize with respect to the value of rating
    :param rat:
    :return: a category (abysmal, awful or bad)
    """
    if rat <= -3:
        category = "abysmal"
    elif -3 < rat <= -1:
        category = "awful"
    else:
        category = "bad"
    return category


# Reading the current csv:
new_data = list()
with open("dad_jokes.csv", mode="r") as original:
    dad_jokes = csv.reader(original)
    headers = next(dad_jokes)
    for row in dad_jokes:
        rating = int(row[-1])
        rating_cat = rating_category(rat=rating)
        row.append(rating_cat)
        new_data.append(row)
headers.append("rating category")
with open("dad_jokes_update.csv", mode="w") as new:
    dad_jokes_updates = csv.writer(new)
    dad_jokes_updates.writerow(headers)
    dad_jokes_updates.writerows(new_data)
