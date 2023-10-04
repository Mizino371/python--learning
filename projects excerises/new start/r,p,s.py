import random
choices = ["rock","paper","scissors"]
def deter_winner (player,computer):
    if player == computer:
        print("Remíza")
        return "Draw"
    elif (
        player == "scissors" and computer == "paper",
        player == "paper" and computer == "rock",
        player == "rock" and computer == "scissors"
    ):
        print("Vyhral si")
        return ("Winner")
    else:
        print("Prehral si 😘")
        return("Loser")

while True:
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    computer_choice = random.choice(choices)
    winner = deter_winner(player_choice.lower,computer_choice.lower)
    print(f"Tvoja voľba {player_choice}, počítač {computer_choice}. {winner}")
    play_again = input("Chceš hrať znova? ")
    if play_again.lower == "ne" or play_again.lower == "nie" :
        break