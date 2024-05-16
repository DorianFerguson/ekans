#!/usr/bin/env python3
import time

import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
p1_score = 0
p2_score = 0
"""The Player class is the parent class for all of the Players
in this game"""

def print_pause(s):
    print(s)
    time.sleep(2)


def print_pause1(s):
    print(s)
    time.sleep(1)

class Player:

    def __init__(self):
        self.my_move = moves
        self.their_move = random.choice(moves)
    

    def move(self):
        return 'rock'
    

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

class Reflect_Player(Player): 

    def move(self):
        return self.their_move
    

    def learn(self, my_move, their_move):
        self.their_move = their_move


class Human_Player(Player):
    def move(self):
        while True:
            move = input("Choose rock, paper, or scissors?\n").lower()
            if move in moves:
                return move
            else:
                print("Invalid move. Please choose again.")

class Random_Player(Player):

    def move(self):
        return random.choice(moves)


def beats(move1, move2):
    if move1 == move2:
        return "It's a Tie!\n"
    elif move1 == 'rock' and move2 == 'scissors' or \
            move1 == 'scissors' and move2 == 'paper' or \
            move1 == 'paper' and move2 == 'rock':
        return 'Player 1 won this round!\n'
    else:
        return 'Player 2 won this round!\n'


class Game:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0


    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause1(f"Player 1 chose {move1}  Player 2 chose {move2}")
        results = beats(move1, move2)
        print(results)
        if "1 won" in results:
            self.p1_score += 1
        elif "2 won" in results:
            self.p2_score += 1
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


    def play_game(self):
        print_pause("The match will begin shortly.")
        for round in range(1,4):
            print(f'Player 1 score:{self.p1_score}\n', f'Player 2 score:{self.p2_score}\n')
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print('Player 1 Wins!')
        elif self.p1_score < self.p2_score:
            print('Player 2 wins!')
        else:
            print("Impressive, you managed too tie 3 times in a row! That's not a win, but it's no small feat.")
        self.play_again()


    def play_again(self):
        choice = input("Game over!, would you like to play again?")
        if choice.lower() == "yes":
            self.p1_score = 0
            self.p2_score = 0
            my_moves = []
            oppponent_moves = []
            self.play_game()
        elif choice.lower() == "no":
         print ("Thanks for playing, goodbye!")
        else:
            print("Invalid input, please enter 'yes' or 'no'")
            self.play_again()

def opponent_select():
    choice = input("""Chose your opponent.
                        1. Random
                        2. Reflect
                        3. Rock\n""")
    if choice == "1":
        return Random_Player()
    if choice == "2":
        return Reflect_Player()
    if choice == "3":
        return Player()

if __name__ == '__main__':
    p1 = opponent_select()
    game = Game(p1, Human_Player())
    game.play_game()
