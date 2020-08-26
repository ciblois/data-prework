print("Let's play!")

gestures = ["paper","rock","scissors"]

n_rounds = int(input("How many rounds would you like to play? ")) 
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

def player_choice():
    print("Choose between",gestures)
    choice = input()
    if (choice == "paper") | (choice == "rock") | (choice == "scissors"):
        return choice
    else:
        return "You type something wrong. Try again."

def cpu_choice():
    import random
    val = random.choice(gestures)
    return val

def res(): #0 if there is a tie, 1 if the computer wins and 2 if the player wins
    if (player_score > cpu_score):
        return "You win!"
    elif (player_score < cpu_score):
        return "The cpu wins!"
    else:
        return "Tie. Try again!"

for i in range(0,n_rounds):
    x = player_choice()
    y = cpu_choice()
    player_score = 0
    cpu_score = 0
    results = {"Tie":0,"cpu":1,"player":2}
    if x == "paper":
        if y == "paper":
            print("The winner is",results["Tie"])
        elif y == "rock":
            print("The cpu choose",results["player"])
            player_score+=1
        elif y == "scissors":
            print("The cpu choose",results["cpu"])
            cpu_score+=1
    elif x == "rock":
        if y == "paper":
            print("The cpu choose",results["cpu"])
            cpu_score+=1
        elif y == "rock":
            print("The winner is",results["Tie"])
        elif y == "scissors":
            print("The cpu choose",results["player"])
            player_score+=1
    elif x == "scissors":
        if y == "paper":
            print("The cpu choose",results["player"])
            player_score+=1
        elif y == "rock":
            print("The cpu choose",results["cpu"])
            cpu_score+=1
        elif y == "scissors":
            print("The winner is",results["Tie"])
    else:
        print("You type something wrong. Try again.")

print(res())