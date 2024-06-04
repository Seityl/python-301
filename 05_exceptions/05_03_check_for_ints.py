# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

def getInt():
    while True:
        try:
            num = int(input("Enter an int: "))
            return num
        except ValueError:
            print("Error! Enter an integer")

try:
    num = getInt()
    print("Your int: ", num)
except:
    print("Error! Enter an integer")
