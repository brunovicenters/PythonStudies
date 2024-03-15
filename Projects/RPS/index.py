from random import randint

print(".....rock, paper, scissors....")

rounds = int(input("How many rounds do you want to play? "))

p1Score = 0
p2Score = 0

i = 0

while i < rounds:
    print(f"Round {i + 1}:")

    p1 = input("enter your move: ").lower()
    if p1 == "quit" or p1 == "q":
        print("\nYou gave up! Rocky would be sad with you...")
        break
    p2 = randint(0, 2)

    # Setting value to computer's choice
    if p2 == 0:
        p2 = "rock"
    elif p2 == 1:
        p2 = "paper"
    elif p2 == 2:
        p2 = "scissors"

    if p1 == "rock" or p1 == "paper" or p1 == "scissors":
        print(f"computer chose: {p2}")
        print("SHOOT!")
        # Verifying who won
        if p1 == p2:
            print("Tie")
        elif p1 == "rock":
            if p2 == "scissors":
                print(f"Player 1 wins round {i+1}!")
                p1Score += 1
            else:
                print(f"Computer wins round {i+1}!")
                p2Score += 1
        elif p1 == "paper":
            if p2 == "rock":
                print(f"Player 1 wins round {i+1}!")
                p1Score += 1
            else:
                print(f"Computer wins round {i+1}!")
                p2Score += 1
        elif p1 == "scissors":
            if p2 == "paper":
                print(f"Player 1 wins round {i+1}!")
                p1Score += 1
            else:
                print(f"Computer wins round {i+1}!")
                p2Score += 1

        if p1Score > rounds / 2 or (i == rounds - 1 and p1Score > p2Score):
            print("\nPlayer 1 wins the match!\n")
            print("*********Score*********")
            print(f"Player 1: {p1Score} | Computer: {p2Score}\n")
            break
        elif p2Score > rounds / 2 or (i == rounds - 1 and p1Score < p2Score):
            print("Computer wins the match!")
            print("*********Score*********")
            print(f"Player 1: {p1Score} | Computer: {p2Score}\n")
            break
        elif i == rounds - 1 and p1Score == p2Score:
            print("It's a tie!")
            print("*********Score*********")
            print(f"Player 1: {p1Score} | Computer: {p2Score}")
    else:
        print("Invalid choice!")
        i -= 1

    i += 1
