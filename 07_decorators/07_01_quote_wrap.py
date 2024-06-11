# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def decorate(text: str):
    result = []
    result = '\"' + text + '\"'
    return result

print(decorate('Hello World!'))