# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable
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

#                                         How to access data in a list

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

#                                                      IN

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

#                                              Loops in lists

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

#                                                 APPEND

# *****************************************************************************************************************

print("\nAPPEND -->")

# You can add a single data to the end of a list using append

games.append("Unbound")
print(f"{games}")
