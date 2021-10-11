
## MULTIPLICATION QUIZ WITHOUT INPUT VALIDATION WITH PYINPUTPLUS

from random import randrange
import time

print("You'll have to complete 10 multiplication exercises")
print("For each exercise you'll have 3 tries")
print("Good luck!")

homework = 0

while homework < 10:

    num1 = randrange(0, 10)
    num2 = randrange(0, 10)
    userInput = input(f"Multiply {num1} x {num2}. What's the result? ")
    result = num1 * num2
    tries = 0


    while tries < 3:
        if int(userInput) == result:
            print("Correct!")
            time.sleep(1)
            tries = 0
            break
        else:
            tries += 1
            if tries == 3:
                print("Wrong! Next question...")
                break
            print("Try again!")
            userInput = input(f"Multiply {num1} x {num2}. What's the result? ")
    

    homework += 1

if homework == 10:
    print("It seems there are no more exercises.")
    print("You have finished. Nice!")
