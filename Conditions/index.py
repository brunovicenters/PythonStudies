# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable
# *****************************************************************************************************************

#                                                   CONDITIONS

# *****************************************************************************************************************

# *****************************************************************************************************************

#                                              COMPARISON OPERATORS

# *****************************************************************************************************************

print("COMPARISON OPERATORS:")

# == - Equal
print(5 == 5)
# != - Not equal
print(5 != 5)
# > - Greater than
print(5 > 5)
# < - Less than
print(5 < 5)
# >= - Greater than or equal
print(5 >= 5)
# <= - Less than or equal
print(5 <= 5)

print(
    "*****************************************************************************************************************"
)

# *****************************************************************************************************************

#                                               LOGICAL OPERATORS

# *****************************************************************************************************************

print("LOGICAL OPERATORS:")

# and - Both conditions must be true --
print(5 == 5 and 6 != 5)

# or - At least one condition must be true --
print(5 == 5 or 5 != 5)

# not - Inverts the result --
print(not 5 == 5)

print(
    "*****************************************************************************************************************"
)

# *****************************************************************************************************************

#                                               If | Elif | Else

# *****************************************************************************************************************

print("IF | ELIF | ELSE:")

# If - Every if statement must have an "if"
# Elif - You can set other conditions with "elif"
# Else - You can set a default condition with "else", in case none of the others is true
grade = 6

if grade >= 6:
    print("Passed!")
elif grade <= 5:
    print("Failed!")
else:
    print("Invalid grade")

print(
    "*****************************************************************************************************************"
)

# Identation is important in if statements --
name = "vyce"

if name == "vyce":
    print("Hello, sir!")
else:
    print("Hey, what's up?")
print("What's your name?")  # This will be printed whatever the if statement is
print(
    "*****************************************************************************************************************"
)

# *****************************************************************************************************************

#                                               TRUTHY | FALSEY

# *****************************************************************************************************************

print("TRUTHY | FALSEY:")

# Some things are naturally false or true --

# Falsey things --
# 1. 0 - Zero
# 2. "" - Empty strings
# 3. None - Empty
# 4. {} - Empty objects
# 5. [] - Empty arrays

# Truthy things --
# 1. Anything else

if []:
    print("Truthy 1")
else:
    print("Falsey 1")

if ["filled"]:
    print("Truthy 2")
else:
    print("Falsey 2")

print(
    "*****************************************************************************************************************"
)

# *****************************************************************************************************************

#                                                     IS

# *****************************************************************************************************************

print("IS:")

# While "==" compares the value of two variables, "is" compares if they're the same item in memory
a = [1, 2, 3]
b = [1, 2, 3]
c = b

print(a == b)  # True
print(a is b)  # False
print(c is b)  # True
