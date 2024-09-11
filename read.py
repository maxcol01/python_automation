# Several ways to read a file:
# 1. Using the open() function -> require to .close()
file = open("jokes.txt", mode="r")
print(file.read())  # read the entire file and return it into a single string !
file.close()
file = open("jokes.txt", mode="r")
print(file.readlines())  # read all the files and put into a list (with \n !!)
file.close()
file = open("jokes.txt", mode="r")
print(file.readline())  # read only the first line !
file.close()

# 2. with open()
with open("jokes.txt", mode="r") as file:
    file1 = file.read()
    file2 = file.readlines()
    file3 = file.readline()

# ok this allows forgetting the .close(). Let's have look at .readlines()

with open("jokes.txt", mode="r") as content:
    lines = content.readlines()

for line in lines:
    print(line.strip())
