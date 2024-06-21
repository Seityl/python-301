# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".
import re

def decorator(func):
    def wrapper(*args):
        # Initialize list of words to be iterated through
        words = []
        print("\nBefore Censoring:\n" + func() + "\n" + "-" * 25)
        print("\nAfter Censoring:\n" + "-" * 25)
        # Remove punctuation from the sentence
        sentence = re.sub(r'[^\w\s]', '', func())
        # Create list of words to be iterated through
        words = func.split(" ")
        for word in words:
            if word in args:
                word = "*" * len(word)
            censoredSentence = [" ".join(word) for word in words]
        return censoredSentence
    return wrapper

@decorator
def sentence(shoot):
    return shoot + "I bumped my toe!"

sentence()