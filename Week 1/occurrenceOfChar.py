
def amountOfTimesCharRepeats(message):
    listOfChars = {}
    mostRepeatedChar = ""
    amountOfTimesRepeated = 0
    mostRepeatedChars = []

    if type(message) == str:
        for char in message:
            listOfChars.setdefault(char, 0)
            listOfChars[char] += 1

        for key, value in listOfChars.items():
            if value > amountOfTimesRepeated:
                mostRepeatedChar = key
                amountOfTimesRepeated = value
                mostRepeatedChars = [[key, value]]
            elif value == amountOfTimesRepeated:
                mostRepeatedChars.append([key, value])

        if len(mostRepeatedChars) > 1:
            return "Most repeated characters were: ", mostRepeatedChars
        else:
            return "Most repeated character was " + mostRepeatedChar.upper() + ", which was repeated " + str(amountOfTimesRepeated) + " times"
    else:
        return TypeError("Error: Argument must be a string!")

print(amountOfTimesCharRepeats(123123)) # error!
print(amountOfTimesCharRepeats("abcabccccbbbaabcbssjfnsaeqq")) # Most repeated character was B, which was repeated 7 times