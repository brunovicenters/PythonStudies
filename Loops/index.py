# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable
# *****************************************************************************************************************

#                                                       LOOPS

# *****************************************************************************************************************

# *****************************************************************************************************************

#                                                        FOR

# *****************************************************************************************************************

print("FOR:")

word = "hello world"

# You can use the "for" keyword to iterate through an iterable object, that can be a string, list, tuple, etc.

# For each item in an iterable object, do the following:
for letter in word:
    print(letter)

print("\n")

# range() can have 3 parameters:
# range(start, stop, step)
# - start: the number to start counting from
# - stop: the number to stop counting
# - step: the number to increment by (even up or down)
# Example:
# range(1, 8, 2) -> 1, 3, 5, 7
# range(8, 1, -2) -> 8, 6, 4, 2
# range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(1, 8) -> 1, 2, 3, 4, 5, 6, 7

for number in range(1, 8):
    print(f"I count to {number}")

# *****************************************************************************************************************

#                                                         WHILE

# *****************************************************************************************************************

print("WHILE:")

im_tired = 0

# While a condition is true, do the following:
while im_tired < 10:
    print("I'm tired")
    im_tired += 1

user_response = input("What do you want to do?")

while user_response != "quit":
    user_response = input("Okay, and what do you want to do now? ")
