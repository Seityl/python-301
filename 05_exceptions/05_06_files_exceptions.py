# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

files = []

# War and Peace File
file1 = "05_exceptions/books/war_and_peace.txt"
with open(file1, 'r', encoding='utf8') as file1:
    file1Content = file1.read()
    files.append(file1Content)

# Crime and Punishment File
file2 = "05_exceptions/books/crime_and_punishment.txt"
with open(file2, 'r+', encoding='utf8') as file2:
    file2.write("")
    file2Content = file2.read()
    files.append(file2Content)

# Pride and Prejudice file
file3 = "05_exceptions/books/pride_and_prejudice.txt"
with open(file3, 'r', encoding='utf8') as file3:
    file3Content = file3.read()
    files.append(file3Content)

for f in files:
    try:
        firstCharacter = f[0][0]
        if firstCharacter:
            print("First Character: ", firstCharacter)
    except Exception as e:
        print(f"Error! {e}")

