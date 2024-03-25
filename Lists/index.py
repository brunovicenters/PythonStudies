# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, while-to-for;for-index-replacement
# *****************************************************************************************************************

#                                                      LISTS

# *****************************************************************************************************************

# *****************************************************************************************************************

#                                               How to create a list

# *****************************************************************************************************************


print("LISTS:")

names = ["Bruno", "Tarsila", "Bárbara", "Joaquim"]

print("\nNames -->")
print(f"{names}")

# To get the length of a list use len()
print(f"There are {len(names)} names in the list.")

print("\nRange in lists -->")
# You can use list() to conver a range into a list
print(f"{list(range(5))}")

# *****************************************************************************************************************

#                                           How to access data in a list

# *****************************************************************************************************************

print("\nAccessing data in lists -->")

# You can access data in a list using the index number
print(f"The first name is {names[0]}")
print(f"The second name is {names[1]}")
print(f"The fourth name is {names[3]}")


print("\nAccessing data in lists in reverse -->")
# You can also use negative indexes, going from the end to the beginning
print(f"The last name is {names[-1]}")
print(f"The second last name is {names[-2]}")
print(f"The third last name is {names[-3]}")

# *****************************************************************************************************************

#                                                       IN

# *****************************************************************************************************************

games = ["Fifa", "League of Legends", "Need For Speed"]

print("\nGames -->")
print(f"{games}")

# You can use "in" to check if something is in a list (it's case-sensitive)
print("\nIN -->")
print(f'Is Fifa in games? {"Fifa" in games}')
print(f'Is need for speed in games? {"Need for Speed" in games}')
print(f'Is NBA2k in games? {"NBA2k" in games}')

# *****************************************************************************************************************

#                                                 Loops in lists

# *****************************************************************************************************************

print("\nLoops in lists -->")

print("\nFor ->")
for game in games:
    print(f"I like to play {game}")

print("\nWhile ->")
i = 0
while i < len(games):
    print(f"I like to play {games[i]}")
    i += 1


# *****************************************************************************************************************

#                                                    APPEND

# *****************************************************************************************************************

print("\nAPPEND -->")

# You can add a single data to the end of a list using append

games.append("Unbound")
print(f"{games}")

# *****************************************************************************************************************

#                                                    EXTEND

# *****************************************************************************************************************

print("\nEXTEND -->")

# You can add multiple data to the end of a list using extend

games.extend(["PUBG", "Rocket League", "Horizon"])
print(f"{games}")

# *****************************************************************************************************************

#                                                     INSERT

# *****************************************************************************************************************

print("\nINSERT -->")

# You can add data in a specific position of a list using insert
games.insert(3, "Minecraft")
print(f"{games}")

print("\nINSERT with negative indexes -->")
# You can use negative indexes
games.insert(-1, "Cuphead")
print(f"{games}")

# *****************************************************************************************************************

#                                                       CLEAR

# *****************************************************************************************************************

print("\nCLEAR -->")

letters = ["a", "b", "c", "d"]
print("\nLetters before clear ->")
print(f"{letters}")

# You can empty a list using clear
letters.clear()
print("\nLetters after clear ->")
print(f"{letters}")

# *****************************************************************************************************************

#                                                       POP

# *****************************************************************************************************************

print("\nPOP -->")

numbers = [1, 2, 3, 4, 5]
print("\nNumbers before pop ->")
print(f"{numbers}")

# You can remove data from a specific position or, in case you don't pass anything, from the end of a list using pop
# PS: Pop returns the removed data
numbers.pop()
print("\nNumbers after pop without index ->")
print(f"{numbers}")

numbers.pop(-2)
print("\nNumbers after pop with index ->")
print(f"{numbers}")

# *****************************************************************************************************************

#                                                      REMOVE

# *****************************************************************************************************************

print("\nREMOVE -->")

names = ["Bruno", "Tarsila", "Abigail", "Bárbara"]
print("\nNames before remove ->")
print(f"{names}")

# You can remove a specific data from a list using remove, removing the first match
# PS: If doesn't find the data, it will raise an error
names.remove("Abigail")

print("\nNames after remove ->")
print(f"{names}")

# *****************************************************************************************************************

#                                                     INDEX

# *****************************************************************************************************************

print("\nINDEX -->")

# You can get the index of a data in a list using index
print(f"The index of Tarsila is {names.index('Tarsila')}")

# You can specify the start and stop indexes
letters = ["a", "b", "c", "d", "b", "e", "f", "b", "g", "h"]
print(f"\nThe index of the second b is {letters.index('b', 2, 8)}")

# *****************************************************************************************************************

#                                                     COUNT

# *****************************************************************************************************************

print("\nCOUNT -->")

# You can count how many times a data appears in a list using count
print(f"The letter b appears {letters.count('b')} times")

# *****************************************************************************************************************

#                                                    REVERSE

# *****************************************************************************************************************

print("\nREVERSE -->")

# You can reverse a list using reverse
names.reverse()
print(f"{names}")

# *****************************************************************************************************************

#                                                     SORT

# *****************************************************************************************************************

print("\nSORT -->")

# You can sort a list in ascending order using sort
print(f"\nNames before sort ->\n{names}")
names.sort()
print(f"\nNames after sort ->\n{names}")

# *****************************************************************************************************************

#                                                     JOIN

# *****************************************************************************************************************

print("\nJOIN -->")

# You can use join to convert a list into a string
words = ["Hello", "my", "name", "is", "Bruno"]
print(" ".join(words))

# *****************************************************************************************************************

#                                                    SLICES

# *****************************************************************************************************************

print("\nSLICES -->")

# You can use slices to get a part of a list, using start and stop indexes, and step, if you want to
# PS: You can pass negative indexes, going from the end to the beginning
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nNumbers ->")
print(f"{nums}")

print("\nNumber after slice with start ->")
print(f"{nums[4:]}")

print("\nNumber after slice with start and end ->")
print(f"{nums[1:6]}")

print("\nNumber after slice with start, end, and step ->")
print(f"{nums[1:10:2]}")

# *****************************************************************************************************************

#                                             Tricks with Slices

# *****************************************************************************************************************

print("\nTricks with slices -->")

# Reversing lists
print("\nReversing lists ->")
print(f"{nums[::-1]}")

# Modifying portions of lists
print("\nModifying portions of lists ->")
nums[1:4] = [0, 0, 0]
print(f"{nums}")

# *****************************************************************************************************************

#                                              Swapping values

# *****************************************************************************************************************

nicknames = ["McCoelho", "Cenourinha"]

print("\nNicknames before swap ->")
print(f"{nicknames}")

nicknames[0], nicknames[1] = nicknames[1], nicknames[0]
print("\nNicknames after swap ->")
print(f"{nicknames}")

# *****************************************************************************************************************

#                                            LISTS COMPREHENSION

# *****************************************************************************************************************

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nNumbers ->")
print(f"{numbers}")

print("\nNumbers squared ->")

# List comprehension is like a for loop in a single line, always returning  a list
# [_expression_   for   _item_   in   _iterable_   *if   _condition_] -> *if is optional
sqrd_numbers = [num**2 for num in numbers if num % 2 == 0]
print(f"{sqrd_numbers}")

# You can also use else
print("\nNumbers even or odd? ->")
even_or_odd = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(f"{even_or_odd}")
