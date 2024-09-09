from pathlib import Path

cwd = Path('.')
print(cwd)

# get the home of our system !
home = Path.home()
print(home)

doc_path = home / 'Desktop'
print(doc_path)

# Check if the path and/or the file we are looking for exist !
if (doc_path / "my_file.txt").exists():
    print('ok the file exists')
    with open(doc_path / "my_file.txt", mode="r") as file:
        content = file.read()
        print(content)
else:
    print('The file does not exist in the referenced folder path')

#  get the parents of our doc_path
print(doc_path.parent)
