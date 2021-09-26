
from random import randrange

def play():
    userChoice = input("choose a weapon! ")
    randomNum = randrange(3)
    computerChoice = ['rock', 'paper', 'scissor']

    if userChoice == computerChoice[randomNum]:
        print('DRAW')
    elif userChoice == 'rock' and computerChoice[randomNum] == 'paper':
        print('computer wins, it chose: ' + computerChoice[randomNum])
    elif userChoice == 'rock' and computerChoice[randomNum] == 'scissor':
        print('user wins, computer chose: ' + computerChoice[randomNum])
    elif userChoice == 'paper' and computerChoice[randomNum] == 'rock':
        print('user wins, computer chose: ' + computerChoice[randomNum])
    elif userChoice == 'paper' and computerChoice[randomNum] == 'scissor':
        print('computer wins, it chose: ' + computerChoice[randomNum])
    elif userChoice == 'scissor' and computerChoice[randomNum] == 'paper':
        print('user wins, computer chose: ' + computerChoice[randomNum])
    elif userChoice == 'scissor' and computerChoice[randomNum] == 'rock':
        print('computer wins, it chose: ' + computerChoice[randomNum])
    else:
        print("That's not a valid weapon!")

play()