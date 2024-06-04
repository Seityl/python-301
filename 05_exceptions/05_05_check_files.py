# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = '05_exceptions\integers.txt'

with open(file_name, 'r') as file:
    fileData = file.read().split("\n",)

try:
    firstValue = int(fileData[0])
except IOError:
    print("Error! IO Error")
except ValueError:
    print("Error! Value Error")
finally:
    result = firstValue * 2
    print("Result: ",result)
