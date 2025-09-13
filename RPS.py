while True:
    choices = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper, or scissors: ").lower()
    import random
    computer = random.choice(choices)
    print("Computer chose:", computer)
    if user == computer:
        print("Tie!")
    elif (user == "rock" and computer == "scissors") or \
        (user == "scissors" and computer == "paper") or \
        (user == "paper" and computer == "rock"):  
            print("You win!")
    else:
        print("HAHA YOU LOSE!")

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break
