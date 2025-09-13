import random

choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

while True:
    #Ask for number of rounds (must be odd)
    rounds = 0
    while rounds % 2 == 0 or rounds <= 0:
        try:
            rounds = int(input("How many rounds? (must be an odd number): "))
            if rounds % 2 == 0 or rounds <= 0:
                print("Please enter a positive odd number (3, 5, 7, ...).")
        except ValueError:
            print("Please enter a valid number.")

    score = {"wins": 0, "losses": 0, "ties": 0}

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        user = input("Choose rock, paper, or scissors: ").lower()

        while user not in choices:
            user = input("Invalid! Please type rock, paper, or scissors: ").lower()

        computer = random.choice(choices)
        print("Computer chose:", computer)

        result = get_winner(user, computer)

        if result == "tie":
            print("It's a tie!")
            score["ties"] += 1
        elif result == "user":
            print("You win this round!")
            score["wins"] += 1
        else:
            print("You lose this round!")
            score["losses"] += 1

        print(f"Current Score -> You: {score['wins']} | Computer: {score['losses']} | Ties: {score['ties']}")

    # Tiebreaker if needed
    while score["wins"] == score["losses"]:
        print("\nIt's a tie! Tiebreaker round!")
        rounds += 1
        print(f"--- Round {rounds} ---")

        user = input("Choose rock, paper, or scissors: ").lower()
        while user not in choices:
            user = input("Invalid! Please type rock, paper, or scissors: ").lower()

        computer = random.choice(choices)
        print("Computer chose:", computer)

        result = get_winner(user, computer)

        if result == "tie":
            print("Still a tie! Another tiebreaker needed...")
            score["ties"] += 1
        elif result == "user":
            print("You win this round!")
            score["wins"] += 1
        else:
            print("You lose this round!")
            score["losses"] += 1

    # Final results
    print("\n=== Final Results ===")
    print("Score:", score)

    if score["wins"] > score["losses"]:
        print("You are the champion!")
    else:
        print("Computer is the champion!")

    # Ask to play again
    again = ""
    while again not in ["y", "n"]:
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again not in ["y", "n"]:
            print("Please enter only 'y' or 'n'.")
    
    if again == "n":
        print("Thanks for playing!")
        break
