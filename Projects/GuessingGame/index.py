from random import randint

while True:
    number = randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    tries = 1

    while guess != number:
        if guess > number:
            print("Too high, try again!")
        else:
            print("Too low, try again!")

        tries += 1
        guess = int(input("Guess a number between 1 and 10: "))

    print(f"You guessed correctly! You took {tries} tries.")

    again = input("Do you want to play again? (y/n) ")

    if again.lower() == "n":
        print("Thanks for playing!")
        break
