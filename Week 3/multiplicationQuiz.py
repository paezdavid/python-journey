
# MULTIPLICATION QUIZ WITHOUT INPUT VALIDATION WITH PYINPUTPLUS

from random import randrange
import time

print("You'll have to complete 10 multiplication exercises")
print("For each exercise you'll have 3 tries")
print("Good luck!")

homework = 0
correctAnswers = 0

while homework < 10:

    num1 = randrange(0, 10)
    num2 = randrange(0, 10)
    userInput = input(f"Multiply {num1} x {num2}. What's the result? ")
    result = num1 * num2
    tries = 0

    try:
        while tries < 3:

            if int(userInput) == result:
                print("Correct!")
                correctAnswers += 1
                tries = 0
                break
            else:
                tries += 1
                if tries == 3:
                    print("Wrong! Next question...")
                    break
                print("Try again!")
                userInput = input(f"Multiply {num1} x {num2}. What's the result? ")
    except ValueError:
        print("Only numbers allowed!")


    homework += 1

if homework == 10:
    print("It seems there are no more exercises.")
    print("You have finished. Nice!")
    print("Score: " + str(correctAnswers) + "/10")





## MULTIPLICATION QUIZ WITH PYINPUTPLUS
## AS SHOWN IN "Automating the Boring Stuff with Python"


# import pyinputplus as pyip
# import random, time

# numberOfQuestions = 10
# correctAnswers = 0
# for questionNumber in range(numberOfQuestions):
#     # Pick two random numbers:
#     num1 = random.randint(0, 9)
#     num2 = random.randint(0, 9)

#     prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

#     try:
#         # Right answers are handled by allowRegexes.
#         # Wrong answers are handled by blockRegexes, with a custom message.
#         pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
#                               blockRegexes=[('.*', 'Incorrect!')],
#                               timeout=8, limit=3)
    
#     except pyip.TimeoutException:
#         print('Out of time!')
#     except pyip.RetryLimitException:
#         print('Out of tries!')

#     else:
#         # This block runs if no exceptions were raised in the try block.
#         print('Correct!')
#         correctAnswers += 1
#         time.sleep(1) # Brief pause to let user see the result.

# print('Score: %s / %s' % (correctAnswers, numberOfQuestions))