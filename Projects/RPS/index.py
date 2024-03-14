from random import randint

print(".....rock, paper, scissors....")

p1 = input("enter your choice:")
p2 = randint(0, 2)

# Setting value to computer's choice
if p2 == 0:
    p2 = "rock"
elif p2 == 1:
    p2 = "paper"
elif p2 == 2:
    p2 = "scissors"

if p1 == "rock" or p1 == "paper" or p1 == "scissors":
    print(f"computer chose {p2}")
    print("SHOOT!")
    # Verifying who won
    if p1 == p2:
        print("Tie")
    elif p1 == "rock":
        if p2 == "scissors":
            print("Player 1 wins!")
        elif p2 == "paper":
            print("Computer wins!")
    elif p1 == "paper":
        if p2 == "rock":
            print("Player 1 wins!")
        elif p2 == "scissors":
            print("Computer wins!")
    elif p1 == "scissors":
        if p2 == "paper":
            print("Player 1 wins!")
        elif p2 == "rock":
            print("Computer wins!")
else:
    print("Invalid choice!")
