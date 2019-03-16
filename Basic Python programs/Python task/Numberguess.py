# -*- coding: utf-8 -*-

"""
Write a program for a Higher / Lower guessing game
The computer randomly generates a sequence of up to 10 numbers
between 1 and 13. The player each after seeing each number
in turn has to decide whether the next number is higher or lower.
If you can remember Brucie’s ‘Play your cards right’ it’s basically
that. If you get 10 guesses right you win the game.
Starting number : 12
Higher(H) or lower(L)? L
Next number 8
Higher(H) or lower(L)? L
Next number 11
You lose
Hints
Use a condition controlled loop (do until, while etc) to control the
game. Do not find yourself repeating the same code over and
over!
You don't need to remember all 10 numbers just the current number
/next number. Don’t forget you’ll have to keep a count of the
number of turns they’ve had.
Extensions
Give the players two lives
Make sure only H or L can
be entered
"""

# Importing random module to generate 10 random number
import random

# Function for performimg game play option
def game_play():
    # Generating 10 random numbers between 1 and 13
    secret_numbers = random.sample(range(1, 13), 10)

    # A varaible to count the wrong guesses
    count = 0

    # A variable to store the player score
    Score = 0

