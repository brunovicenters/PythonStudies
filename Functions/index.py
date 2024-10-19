# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, dict-assign-update-to-union, while-to-for, for-index-replacement, remove-dict-keys, unwrap-iterable-construction, remove-duplicate-set-key;
# *****************************************************************************************************************

#                                                  FUNCTIONS

# *****************************************************************************************************************

# *****************************************************************************************************************

#                                               Functions basics

# *****************************************************************************************************************

print("\nFUNCTIONS:")


# To define a function use def
def say_hello():
    print("\nHello World!\n")


# To call a function use function_name()
say_hello()


# To define a function with parameters pass them inside the parentesis (you can define it's type if you want)
def happy_birthday(name: str):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print(f"Happy Birthday dear {name}!")
    print("Happy Birthday to you!\n")


happy_birthday("Tarsila")

# *****************************************************************************************************************

#                                               Return

# *****************************************************************************************************************

print("\nRETURN:")


# To return a value use return
def square_of(num: int):
    return num**2


sqr = square_of(5)

print(f"\nSquare of 5 -> {sqr}\n")


# You can also define the return type
def even_or_odd(num: int) -> str:
    return "even" if num % 2 == 0 else "odd"


print(f"\nIs 5 even or odd? -> {even_or_odd(5)}\n")

# *****************************************************************************************************************

#                                               Global

# *****************************************************************************************************************

print("\nGlobal:")

# You can have access to global variables inside a function with the keyword global

x = 5
y = 10


def multiply():
    global x
    global y
    return x * y


print(f"\n{x} * {y} = {multiply()}\n")

# *****************************************************************************************************************

#                                                   Docstring

# *****************************************************************************************************************

print("\nDocstring:")

# You can add documentation to your functions using the docstring


def exponent(num, power=2):
    """exponent(num, power) -> num to specified power. Power defaults to 2"""

    return num**power


print(exponent(5, 3))
print(exponent.__doc__)


# *****************************************************************************************************************

#                                                   Star args

# *****************************************************************************************************************

print("\nStar args:")

# You can pass any number of arguments to a function using the *


def sum_all_nums(*nums):

    return sum(nums)


print(sum_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
