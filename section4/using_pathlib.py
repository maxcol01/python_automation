from pathlib import Path

cwd = Path('.')
print(cwd)

home = Path.home()
print(home)

doc_path = home / 'Desktop'
print(doc_path)

if (doc_path/"my_file.txt").exists():
    print('ok')
else:
    print('ko')

with open(doc_path/"my_file.txt", mode="r") as file:
    content = file.read()
    print(content)