# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

# Creates custom exception from existing exception class
class customException(Exception):
    def __init__(self, message="An error has occured"):
        self.message = message
        super().__init__(self.message)
    
# Searches for 'prince' in the first 100 characters of each file in an array of files
def findPrince(text):
    first100 = text[:100]
    if 'prince' in first100.lower():
        return True
    else:
        return False 

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
        if findPrince(f):
            print(f"True")
        else:
            print(f"False")
    except:
        print("Error!")