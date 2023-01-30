
def appendToFile():
    # to append to the file, use the mode='a'
    with open('test.txt', mode='a') as my_file:
        text = my_file.write('hey its me')
        print(text) 

# mode='w' create a new file
# create a new file from user input
def createNewFile():
    new_file_name = input(f"whats the name of the new text file you want to craete? ")
    with open(f"{new_file_name}.txt", mode='w') as my_file:
        opening_text = my_file.write("your new file")
        print(opening_text) 

print(createNewFile())


