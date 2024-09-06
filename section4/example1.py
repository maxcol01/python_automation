#  this is a relative path. If we want the absolute path, we need to reference the root of our systm
path = "../../section3/pythonProject/"

with open(path+"jokes.txt", mode="r") as file:
    content = file.read()
    print(content)
