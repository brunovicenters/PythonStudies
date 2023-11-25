# *****************************************************************************************************************

#                                                                    Strings

# *****************************************************************************************************************

# You can use double quotes or single quotes to create strings --
print("Hello world!!")
print('Hello world!!')

# And you can even use them together --
print("\nShe said 'Hello world!!'\n")

# *****************************************************************************************************************

#                                                               Escape Sequences

# *****************************************************************************************************************

# You can use \n to skip a line --
print("Hello\nWorld")

# To write a "\" use "\\" --
print("\nThis is a backslash: \\ ")

# You also can use \" or \' to write quotes --
print("\nThis is a \"quote\" and", 'this is another \'quote\'')

# *****************************************************************************************************************

#                                                                  f-strings

# *****************************************************************************************************************

# You can also print using f-string, to show values without concatenating --
name = "Vicente"
print(f"\nMy name is {name}")

# *****************************************************************************************************************

#                                                               String indexes

# *****************************************************************************************************************

positive = "yes"
negative = "no"

print(f"\nFor yes, type {positive[0]}, for no, type {negative[0]}")