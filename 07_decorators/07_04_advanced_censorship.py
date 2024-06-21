# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def decorator(function):
    takingInput = True
    while takingInput == True:
        words = []
        word = str(input("Enter the word that you would like to be censored:"))
        print("Type '1' to stop accepting words")
        if word == '1':
            takingInput == False
        else:
            words.append(word)
    def censor(*args'):
        print("\nBefore Censoring:\n" + "-" * 25)
        result = function(*args)
        print(result)
        print("\nAfter Censoring:\n" + "-" * 25)
        sentences = result.split("!")
        censoredSentences = []
        for sentence in sentences:
            words = sentence.split(" ")
            censoredWords = []
            for word in words:
                if "!" in word:
                    word = word.replace("!", "")
                if word.lower() == "shoot":
                    censoredWords.append("S****")
                else:
                    censoredWords.append(word)
            censoredSentence = " ".join(censoredWords)
            censoredSentences.append(censoredSentence + "!")
        return " ".join(censoredSentences)
    return censor

@decorator
def sentence(oWord):
    return "I bumped my toe! " + oWord

print(sentence('Shoot!'))