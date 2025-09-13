import random

choices = ["rock", "paper", "scissors"]

score = {"wins": 0, "losses": 0, "ties": 0}

while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice, try again.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
        score["ties"] += 1
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
        score["wins"] += 1
    else:
        print("You lose!")
        score["losses"] += 1

    print("Score:", score)

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break
