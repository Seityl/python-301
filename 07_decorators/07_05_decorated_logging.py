# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import re
from datetime import datetime

def splitSentence(sentence):
    # Defines pattern to match words and punctuation
    pattern = r"[\w']+|[.,!?;]"
    # Split sentence based on the pattern using re.findall
    tokens = re.findall(pattern, sentence)
    # Return the split sentence
    return tokens

def decorator(func):
    def wrapper():
        # Sets variable originalSentence to the return value of the ORIGINAL FUNCTION
        originalSentence = func()

        # EXECUTED AFTER CALLING ORIGINAL FUNCTION
        
        print("\nBefore Censoring:\n\n" + originalSentence + "\n" + "-" * 100)

        # Initialize list of words to be censored
        wordsToCensor = []
        while True:
            word = input("Enter a word that you wish to censor('1' to STOP): ")
            if word:
                if word == "1":
                    break
                elif word in wordsToCensor:
                    print("Error! You are already censoring this word.")
                else:
                    wordsToCensor.append(word)

        # Split sentence into list of words and punctiation
        sentenceWords = splitSentence(originalSentence)

        # Censor words in the sentence while preserving capitalization
        censoredSentence = []
        for word in sentenceWords:
            if word.isalpha() and word.lower() in [w.lower() for w in wordsToCensor]:
                censored_word = word[0] + "*" * (len(word) - 1)
                # Preserve capitalization
                if word.istitle():  # Check if the word is title-cased
                    censored_word = censored_word.capitalize()
                elif word.isupper():  # Check if the word is all uppercase
                    censored_word = censored_word.upper()
                censoredSentence.append(censored_word)
            else:
                censoredSentence.append(word)

         # Join censored words into a sentence
        censored_sentence = ""
        for i, word in enumerate(censoredSentence):
            if re.match(r"[.,!?;]", word) and i > 0:
                censored_sentence += word  # Append punctuation marks without leading space
            else:
                censored_sentence += " " + word  # Append words with leading space
        
        # Remove leading space from the beginning of the sentence
        censored_sentence = censored_sentence.lstrip()
        print("\nAfter Censoring:\n" + censored_sentence + "\n" + "-" * 100)
        return censored_sentence
    return wrapper

def logger(func):
    def wrapper():
        result = func()
        print(f"Function {func.__name__} was called at {datetime.now()}")
        return result
    return wrapper

@logger
@decorator
def sentence():
    while True:
        originalSentence = input("Please Enter Sentence: ")
        if originalSentence:
            return originalSentence    

print(sentence())