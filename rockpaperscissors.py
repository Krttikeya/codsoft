#rockpaperscissors 14 aug
import random
options = ("rock", "paper", "scissors")
playagain="yes"
while playagain=="yes":
    playerChoice = None
    pcChoice = random.choice(options)
    while playerChoice not in options:
        playerChoice = input("choose.. \n\n 1. Rock \n 2. Paper \n 3. Scissors \n")

    print(f"player: {playerChoice}")
    print(f"pc: {pcChoice}\n ")

    if playerChoice== pcChoice:
        print("It's a tie!")
    elif playerChoice == "rock" and pcChoice == "scissors":
        print("You win!")
    elif playerChoice == "paper" and pcChoice == "rock":
        print("You win!")
    elif playerChoice == "scissors" and pcChoice == "paper":
        print("You win!")
    elif pcChoice == "rock" and playerChoice == "scissors":
        print("You lose!")
    elif pcChoice == "paper" and playerChoice == "rock":
        print("You lose!")
    elif pcChoice == "scissors" and playerChoice == "paper":
        print("You lose!")
    print()

    playagain = input("Play again?\n")
