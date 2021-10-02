import re, pyperclip

stringToAnalyze = pyperclip.paste()

def find_number(stringToAnalyze):
    # phoneNumberRegex is based on the Paraguayan telephone number system
    phoneNumberRegex = re.compile(r'''
        (\(\d{4}\)|\d{4}) # 4 first digits with or without parentheses
        (\s|-|\.)? # optional separator
        (\d{3}) # 3 digits
        (\s|-|\.)? # optional separator
        (\d{3}) # 3 digits
    ''', re.VERBOSE)

    # findall returns a list of tuples
    # each tuple contains all the groups inside our regex pattern
    listOfTuples = phoneNumberRegex.findall(stringToAnalyze)
    listOfNumbers = []
    for tuple in listOfTuples:
        listOfNumbers.append(''.join(tuple))

    return listOfNumbers


def find_email(stringToAnalyze):
    emailRegex = re.compile(r'''
        ([a-zA-Z0-9._-]+)
        (@)
        ([a-zA-Z]+)
        (\.[a-zA-Z]{3,4})
        (\.[a-zA-Z]{,2})?
    ''', re.VERBOSE)

    # findall returns a list of tuples
    # each tuple contains all the groups inside our regex pattern
    listOfTuples = emailRegex.findall(stringToAnalyze)
    listOfEmails = []
    for tuple in listOfTuples:
        listOfEmails.append(''.join(tuple))

    return listOfEmails


def find_emails_and_numbers(stringToAnalyze):
    emailsAndNum = []

    emailsAndNum.append('\n'.join(find_email(stringToAnalyze)))
    emailsAndNum.append('\n'.join(find_number(stringToAnalyze)))

    # If the program doesn't find anything
    # emailsAndNum will be an array with two empty strings
    if emailsAndNum == ['', '']:
        return "No emails or phone numbers found"
    else:
        return ' '.join(emailsAndNum)


print(find_emails_and_numbers(stringToAnalyze))