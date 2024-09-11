from pathlib import Path
from datetime import datetime

#  What if we need to deal with several path to our files ?
# python embeds the iterdir() method -> generate an iterator of the files and folder in
# another folder allowing to iterate over !

# Path object of the directory  we want to iterate over

# path = Path.home() / 'to_the_folder'
path = Path('.')
# using the following we can have access to many properties and methods !
for item in path.iterdir():
    # this provides us a path to every files in our folder !
    # check if the item is a file
    # .stem allows to remove the suffix of the name we want to print !
    print(item)
    if item.is_file() and item.suffix == ".txt":
        print(item.stem, 'is a file')
        # .stat() available on a path object !
        stats = item.stat()
        print('Size:', stats.st_size)
        print("Last modified:", datetime.fromtimestamp(stats.st_mtime))
    # check if it is a directory
    if item.is_dir():
        print(item.name, 'is a directory')

    if "read" in item.name.lower():
        print("read is part of the file or folder name")
