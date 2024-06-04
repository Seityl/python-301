# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

def divideNumbers(num1, num2):
    try:
        quotient = num1/num2
        return quotient
    except ZeroDivisionError:
        print("Error! Zero Divison Error")
    else:
        print("Divison successful")
        return quotient

quotient = divideNumbers(1, 1)
if quotient is not None:
    print("Quotient: ", quotient)