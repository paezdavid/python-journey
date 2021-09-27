
import random, time

def reversedGuessTheNumber():
    try:
        userNumber = int(input("Choose a number between 1 and 20 for the computer to guess: ")) 

        if userNumber > 20:
            print("The number to guess should be less than 21")
            return
        
        print("Hey computer, I'm thinking of a number between 1 and 20, can you guess it?")

        attempts = 0

        while attempts < 6:
            print("Guessing...")
            computerGuess = random.randrange(1, 21)
            print(computerGuess)
            attempts += 1

            # I used time.sleep() here so that the program runs more slowly
            # and we could see how the computer guesses each time
            time.sleep(0.5)

            if computerGuess == userNumber:
                print("Well done, computer! The number was " + str(userNumber) + " and it took you " + str(attempts) + " attempt(s) to guess it")
                break
            elif attempts == 6:
                print("The computer was not able to guess the number.")
                break

    except ValueError:
        print("You should input a number! Try again.")

reversedGuessTheNumber()