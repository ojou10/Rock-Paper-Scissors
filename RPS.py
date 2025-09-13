import random

choices = ["rock", "paper", "scissors"]

while True:
    rounds = 3
    score = {"wins": 0, "losses": 0, "ties": 0}

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        user = input("Choose rock, paper, or scissors: ").lower()

        # Validate choice
        while user not in choices:
            user = input("Invalid! Please type rock, paper, or scissors: ").lower()

        computer = random.choice(choices)
        print("Computer chose:", computer)

        if user == computer:
            print("It's a tie!")
            score["ties"] += 1
        elif (user == "rock" and computer == "scissors") or \
             (user == "scissors" and computer == "paper") or \
             (user == "paper" and computer == "rock"):
            print("You win this round!")
            score["wins"] += 1
        else:
            print("You lose this round!")
            score["losses"] += 1

    # After all rounds, show results
    print("\n=== Final Results ===")
    print("Score:", score)

    if score["wins"] > score["losses"]:
        print("You are the champion!")
    elif score["losses"] > score["wins"]:
        print("Computer is the champion!")
    else:
        print("It's a tie overall!")

    # Ask to play again (validated)
    again = ""
    while again not in ["y", "n"]:
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again not in ["y", "n"]:
            print("Please enter only 'y' or 'n'.")
    
    if again == "n":
        print("Thanks for playing!")
        break
