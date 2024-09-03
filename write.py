poem = [("Roses", "red"), ("Violet", "blue"),
        ("Sugar", "sweet")
        ]

text = ""
for item in poem:
    if item[0] == "Sugar":
        text += f"{item[0]} is {item[1]}\n"
    else:
        text += f"{item[0]} are {item[1]}\n"

text += "And so are you !\n"

# using write mode will create the file if it does not exist !
# also: write erase the previous text !
with open("writeTo.txt", mode="w") as file:
    file.write(text)
#with open("writeTo.txt", mode="w") as file:
#    file.write("et moi peduuuu") # this erased the poem !

# to add to an existing file: .wite() but in append mode !

with open("writeTo.txt", mode="a") as file:
    file.write("et moi peduuuu \n")
