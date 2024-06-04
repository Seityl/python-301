# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

def getNumber(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Enter a valid number")

try:
    dividend = getNumber("Enter dividend: ")
    divisor = getNumber("Enter divisor: ")

    if divisor == 0:
        raise ZeroDivisionError("Error! Can't divide by 0")
    
    quotient = dividend / divisor
    print(f"Quotient: {quotient}")
except ZeroDivisionError as e:
    print("Error: ",e)
except Exception as e:
    print("Error: An unknown error has occured")