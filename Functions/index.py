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
