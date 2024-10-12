# The hangman game
import random

end = False
lifes = 6
guesses = []

print("Welcome to Hangman Code!")

foods = ["apple", "orange", "potato", "cheese", "rice", "chicken", "pasta"]
langs = ["python", "java", "javascript", "golang", "ruby", "php", "rust"]
names = ["Tarsila", "Bruno", "Bernardo", "Cecília", "Stacy", "Chandler", "Rachel"]

print("Qual tema você deseja?")
print("1 - Food\n2 - Code Languages\n3 - Names\n0 - Exit")
theme = int(input())

match theme:
    case 0:
        end = True
        print("Goodbye!")
    case 1:
        word = random.choice(foods).lower()
    case 2:
        word = random.choice(langs).lower()
    case 3:
        word = random.choice(names).lower()
    case _:
        end = True
        print("Wrong input!")

while end == False:

    if lifes == 0:
        print(f"\nYou've {lifes} lifes")
        print("\n\nYOU LOST!!")
        end = True
        break

    if all(letter in guesses for letter in word):
        print(f"\nCongratulations! You've guessed the word: {word}")
        print("YOU WIN!!")
        end = True
        break

    print(f"You have {lifes} lifes left.")

    if len(guesses) > 0:
        print(f"You have guessed the following letters:")
        print("".join([char + " - " for char in guesses]))

    print("".join([char if char in guesses else " _ " for char in word]) + "\n")

    guess = input("Guess a letter:\n").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please, enter a single letter!\n")
        continue

    if guess in guesses:
        print("You've already guessed this letter!\n")
        continue

    guesses.append(guess)

    if guess in word:
        print(f"You're right! There is a {guess} in this word!")
    else:
        print(f"You've guessed wrong! There is no {guess} in this word!")
        lifes -= 1
