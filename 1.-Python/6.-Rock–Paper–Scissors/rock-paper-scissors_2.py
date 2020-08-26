# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:05:19 2020

@author: Cinthya Blois
"""

print("Let's play!")

gestures = ["paper","rock","scissors"]

n_rounds = int(input("What is the maximum number of plays you want to have? ")) 
#the maximum number of rounds to play in a game. Must be odd numbers
if (n_rounds %2 == 0):
    print("The number must be odd.")
    n_rounds = int(input("Please, type again. "))
else:
    pass

rounds_to_win = int(input("How many rounds a player must win to win the game? "))
#the value stored in rounds_to_win depends on the value of n_rounds.
if rounds_to_win > n_rounds:
    print("The number must be smaller than the number of rounds.")
    n_rounds = int(input("Please, type again. "))
else:
    pass

player_score = 0
cpu_score = 0

def player_choice():
    print("Choose between",gestures)
    choice = input()
    if (choice == "paper") | (choice == "rock") | (choice == "scissors"):
        return choice
    else:
        print("You type something wrong. Try again.")

def cpu_choice():
    import random
    val = random.choice(gestures)
    return val

def res(x,y): #0 if there is a tie, 1 if the computer wins and 2 if the player wins
    if x == "paper":
        if y == "paper":
            return 0
        elif y == "rock":
            return 2
        elif y == "scissors":
            return 1
    elif x == "rock":
        if y == "paper":
            return 1
        elif y == "rock":
            return 0
        elif y == "scissors":
            return 2
    elif x == "scissors":
        if y == "paper":
            return 2
        elif y == "rock":
            return 1
        elif y == "scissors":
            return 0
    else:
        return "You type something wrong. Try again."

def round_res():
    x = player_choice()
    y = cpu_choice()
    r = res(x,y)
    global player_score
    global cpu_score
    if r == 1:
        cpu_score +=1
    elif r == 2:
        player_score +=1
    else:
        pass
    print("Player's choice: ",x)
    print("Cpu's choice: ",y)
    print("Round win is ",r)
    
for i in range(0,n_rounds):
    x = round_res()
    print("Player's score:",player_score)
    print("Cpu's score",cpu_score)
    if (player_score == rounds_to_win) | (cpu_score == rounds_to_win):
        print(x)
        if (player_score == rounds_to_win):
            print("The final winner is you!")
        elif (cpu_score == rounds_to_win):
            print("The final winner is cpu!")
        break
    elif i == n_rounds-1:
    #elif (player_score < rounds_to_win) & (cpu_score < rounds_to_win):
        print("The maximum number of rounds was not enough to obtain the condition to win the game.")
    else:
        continue