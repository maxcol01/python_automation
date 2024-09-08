#  this is a relative path. If we want the absolute path, we need to reference the root of our systm
path = "../../section3/pythonProject/"

with open(path + "jokes.txt", mode="r") as file:
    content = file.read()
    print(content)

#  the problem here is the fact that depending on the OS we may have different way
#  to write the path ! so we need to use Pathlib !
