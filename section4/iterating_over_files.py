from pathlib import Path

#  What if we need to deal with several path to our files ?
# python embeds the iterdir() method -> generate an iterator of the files and folder in
# another folder allowing to iterate over !

# Path object of the directory  we want to iterate over

path = Path.home() / 'to_the_folder'

# using the following we can have access to many properties and methods !
for item in path.iterdir():
    # this provides us a path to every files in our folder !
    #check if the item is a file
    if item.is_file() and item.suffix == ".txt":
        print(item.name, 'is a file')

    # check if it is a directory
    if item.is_dir():
        print(item.name, 'is a directory')
