# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

# TODO: FINISH PLEASE

def decorator(function):
    def censor(*args):
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
