
with open("fruits.txt") as file:
    content = file.read()

with open("first.txt") as file:
    file.write(content[:90])
