# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(function):
    def decorateString(*args):
        print("\nBefore Decorating:\n")
        result = function(*args)
        print(result)
        print("\nAfter Decorating:\n")
        result = "*" * 20 + "\n" + function(*args) + "\n"  + "*" * 20
        return result
    return decorateString

@decorate
def userString(s):
    return s

print(userString("Hello"))