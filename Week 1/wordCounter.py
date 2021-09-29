import pyperclip

def countWords():
    copiedText = pyperclip.paste()
    listOfWords = copiedText.split()

    # remove \r\n after some words
    for char in listOfWords:
        char.rstrip()

    print(f"Total amount of characters: {len(' '.join(listOfWords))}")
    print(f"Total amount of words: {len(listOfWords)}")

countWords()

