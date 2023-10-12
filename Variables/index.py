# To declare variables, you need to use the following structure --
# <var_name> = <value>
# Some rules, restrictions and conventions to name your variables ar:
# 1 - Must start with a letter or underscore;
# 2 - The rest of the name must contain letters, underscores, or numbers, only;
# 3 - Variables' name are case-sensitive;
# 4 - Variables should be snake_case (Separated by underscore[_]);
# 5 - Variables should be lower case, with some exceptions:
#       1 - CAPITAL_SNAKE_CASE are usually for constants;
#       2 - UpperCamelCase are usually for classes;
# 6 - Variables with double underscores at the beginning and at the end are supposed to be private or left alone (__dont_touch__);

# To store a string --
string = "Hello world"

# To store a number --
num = 10

# To store an array --
arr = [1, 2, 3, 4]

# To store an object --
obj = {1, 2, 3, 4}

# To store a boolean --
tr = True
fl = False

# You can also store more than one variable per line
# separating them by commas --
username, password, email, active = (
    "Patolinors",
    "12345",
    "Patolino.dev@gmail.com",
    True,
)

print("String:\n" + string + "\n")

print("Number:\n", num, "\n")

print("Array:\n", arr, "\n")

print("Object:\n", obj, "\n")

print("Boolean:\n", tr, "|", fl, "\n")

print(
    "Account details:\n",
    "Username:",
    username,
    "\n",
    "Password:",
    password,
    "\n",
    "Email:",
    email,
    "\n",
    "Active:",
    active,
    "\n",
)
