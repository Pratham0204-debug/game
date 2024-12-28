import random
players = ["snake", "water", "gun"]

user = input("Enter a choice: ")
comp = random.choice(players)
print(comp)

def play_game(user, comp):
 
    if user == comp:
        return 0
    if user == "snake" and comp == "gun":
        return -1
    elif user == "water" and comp == "snake":
        return -1
    elif user == "gun" and comp == "water":
        return -1
    else:
        return 1

score = play_game(user, comp)

if score == 0:
    print("Tie")
elif score == 1:
    print("You win")
else:
    print("You lose")