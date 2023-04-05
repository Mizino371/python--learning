import random


def play():
    user = input (" r for rock, p for paper, s for scissors")
    computer = random.choice(["r , p, s"])

    if user == computer :
        return "tie"
    
    if is_win(user, computer):
        print ("You are winner")

    return "You lost !"
    
def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player =="p" and opponent == "r") or (player == "s" and opponent == "p"):
        print ("You are winner")

print(play())