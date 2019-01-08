# -*- coding: utf-8 -*-

# To select random values we use random module
# random.choice(List) - selects the random value from a list
import random

# to generate random words random_words module is used
# importing RandomWords from random_words to generate a random words
# from random_word import RandomWords

# opening a file for getting the values for the list
# using with keyword as it is autocloseable
with open("words.txt", "r") as fileobj:
    list1 = fileobj.read().splitlines()

# Generating the random words and creating the other variables required for further operations
ran_word = random.choice(list1)
secret_word = "-"*len(ran_word)


print("--------HANGMAN LETTER GAME-------".center(20))
chance = len(ran_word)
print("Lifes:", chance)
print("GUESS A FRUIT NAME:", secret_word)
print("Type quit to escape")


# craeting a function for performing the operation for the game
def game_play(word, chances):
    # To create a replica for the random word to use in any further operation
    repl = word

    Wrong_guess = 0

    # To take user input
    for var in range(0, chances):
        user_input = input(">")
        user_input = user_input.lower()
        if user_input in repl:
            repl = repl.replace(user_input, "", 1)
            print(user_input+" found ")
        elif user_input == "quit":
            break
        else:
            print("Letter not found")
            Wrong_guess = Wrong_guess + 1
    if Wrong_guess >= 2:
        print("You loose")
    elif Wrong_guess <= 1 and var == chances-1:
        print("You win")
    elif Wrong_guess <= 1 and var != chances-1:
        print("You left the game in middle")


# Function call
game_play(ran_word, chance)

print("Original Word:", ran_word)
