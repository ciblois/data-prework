# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:05:19 2020

@author: Cinthya Blois
"""

print("Let's play!")

gestures = ["paper","rock","scissors"]

n_rounds = int(input("How many rounds would you like to play?")) #the maximum number of rounds to play in a game. Must be odd numbers
rounds_to_win = 0

print("Choose between",gestures)
choice = input()
import random
cpu_choice = random.choice(gestures)
print(cpu_choice)

#checking the game
#player_moves = []
#cpu_moves = []
#player_moves.append(choice)
#cpu_moves.append(cpu_choice)

player_score = 0
cpu_score = 0

if (choice == "paper") & (cpu_choice == "paper"):
    print("The cpu choose", cpu_choice,". Tie")
elif (choice == "paper") & (cpu_choice == "rock"):
    print("The cpu choose", cpu_choice,". You win!")
    player_score+=1
elif (choice == "paper") & (cpu_choice == "scissors"):
    print("The cpu choose", cpu_choice,". The cpu wins!")
    cpu_score+=1
elif (choice == "rock") & (cpu_choice == "paper"):
    print("The cpu choose", cpu_choice,". The cpu wins!")
    cpu_score+=1
elif (choice == "rock") & (cpu_choice == "rock"):
    print("The cpu choose", cpu_choice,". Tie")
elif (choice == "rock") & (cpu_choice == "scissors"):
    print("The cpu choose", cpu_choice,". You win!")
    player_score+=1
elif (choice == "scissors") & (cpu_choice == "paper"):
    print("The cpu choose", cpu_choice,". You win!")
    player_score+=1
elif (choice == "scissors") & (cpu_choice == "rock"):
    print("The cpu choose", cpu_choice,". The cpu wins!")
    cpu_score+=1
elif (choice == "scissors") & (cpu_choice == "scissors"):
    print("The cpu choose", cpu_choice,". Tie")
else:
    print("You type something wrong. Try again.")

if player_score > cpu_score:
    print("You win",player_score,"times and cpu", cpu_score,"times. So you are the winner!")
elif player_score < cpu_score:
    print("You win",player_score,"times and cpu", cpu_score,"times. So the cpu are the winner!")
else:
    print("You win",player_score,"times and cpu", cpu_score,"times. Try again!")