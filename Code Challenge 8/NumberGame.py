# -*- coding: utf-8 -*-

# For getting random number importing random
import random

# Creating the computer guess
secret_number = random.randint(1, 10)

# Initializing the no. of chances given to user
chances = 6

print("******************* NUMBER GAME APP ***************************")
print("Guess a number until you win")


# Defining a format function for printing the guesses after player loose
def Format(y):
    print("Player guess:", y)


# Taking user input
def game_play(tries):
    while(tries > 0):
        guess_number = input(">")
        if guess_number.isalpha():
            print("Wrong input")
        else:
            if int(guess_number) == secret_number:
                print("Player wins and Computer loose")
                break
            elif int(guess_number) > 10:
                print("Too high")
            elif int(guess_number) < 1:
                print("Too low")
            else:
                print("Computer wins and player looses")
                Format(guess_number)
        tries = tries-1
        print("Chances left:", tries)


game_play(chances)
option = input("Wanna play again Y/N?")
if (option.upper()) == 'Y':
    game_play(chances)
else:
    pass
