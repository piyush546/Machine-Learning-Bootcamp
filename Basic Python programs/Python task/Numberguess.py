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

print("****************Welcome To Number Guess Game*************************")
lives = int(input("Before Starting the Game set your lives here:"))
print("Your game start nows")


# Designing the class for game playing operation
class Game_play():

    # Initializing the starting range and ending range of the game numbers
    def __init__(self, start, end, size):
        self.start = start
        self.end = end
        self.size = size
        self.numbers = random.sample(range(self.start, self.end), self.size)

    # Function to return the magic numbers
    def numbers_selector(self, index):
        self.index = index
        return self.numbers[self.index], self.numbers[index-1]

    # Function to initialize the Player's choice
    def players_choice(self):
        self.guess = input('Higher(H)/Lower(L):')
        return self.guess

    # Function to operate the game
    def game_master(self):
        # Variable to store wrong guess point
        self.loose = 0

        # Variable to store right guess point
        self.win = 0

        print("Starting number:", self.numbers[0])
        self.count = 1
        while (self.loose < 2) or (self.win == self.size - 1) or (self.count == self.size-1):

            # Function calls
            self.response = self.players_choice()
            self.n_f, self.n_b = self.numbers_selector(self.count)

            print("Next number:", self.n_f)
            if(self.response == 'H' and self.n_f > self.n_b) or (self.response == 'L' and self.n_f < self.n_b):
                self.win += 1
            else:
                self.loose += 1
            self.count += 1

        print("Game Ended")
        if self.loose == 2:
            print("You Loose")
        else:
            print("You win")


# A function to operate the basics for class objects and numbers input
def main_game():
    print("Set your range between which you want to choose magic numbers")
    start_n = int(input("Enter the starting number of the magic range:"))
    end_n = int(input("Enter the ending number of the magic range:"))
    size_repl = int(input("Enter the size of the magic numbers collection:"))
    obj = Game_play(start_n, end_n, size_repl)
    obj.game_master()


# Initial function call
main_game()

# Checking for Player's interest either want to continue or quit
for var in range(1, lives):
    option = input("Want to play again Y/N?:")
    if option == 'Y':
        print("Greetings! You're back again")
        main_game()
    else:
        print("See you again")
        break
