# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, while-to-for, for-index-replacement,for-index-underscore, identity-comprehension;
print("Exercises:")

# LIST COMPREHENSION -->
print("LIST COMPREHENSION -->")

# Get the first letter of each name
answer = [item[0] for item in ["Ellie", "Tim", "Matt"]]
print(f"\nFirst letters -> {answer}\n")

# Get the even numbers
answer = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(f"\nEven Numbers -> {answer}\n")

# Get the intersection between the lists
answer = [num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6]]
print(f"\nIntersection -> {answer}\n")

# Lowercase and reverse each name
answer = [word[::-1].lower() for word in ["Elie", "Tim", "Matt"]]
print(f"\nLower and Reverse -> {answer}\n")

# Get the numbers divisible by 12
answer = [num for num in range(1, 101) if num % 12 == 0]
print(f"\nDivisible by 12 -> {answer}\n")

# Write the string without the vowels
answer = "".join([char for char in "amazing" if char not in "aeiou"])
print(f"\nOnly consonants -> {answer}\n")

# Write [[0,1,2],[0,1,2],[0,1,2]] using nested list comprehension
answer = [[num for num in range(3)] for item in range(3)]
print(f"Nested list comprehension -> {answer}")
