# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, while-to-for, for-index-replacement, remove-dict-keys
# *****************************************************************************************************************

#                                                    DICTIONARY

# *****************************************************************************************************************

# *****************************************************************************************************************

#                                            How to a create a dictionary

# *****************************************************************************************************************

print("\nDICTIONARY:")

# To create a dictionary you use {}, and you add items with keys and values
cart_item = {"name": "Milk", "price": 3.99, "quantity": 5}
print(f"\nCart item -> {cart_item}")
print(f"Cart item name -> {cart_item['name']}")
print(f"Cart item price -> {cart_item['price']}")
print(f"Cart item quantity -> {cart_item['quantity']}")

# *****************************************************************************************************************

#                                               Lists with dictionary

# *****************************************************************************************************************

print("\nShopping cart:")
shopping_cart = [
    {"name": "Milk", "price": 3.99, "quantity": 5},
    {"name": "Bread", "price": 2.99, "quantity": 10},
    {"name": "Eggs", "price": 0.99, "quantity": 20},
]

for item in shopping_cart:
    print(f"{item['name']} ...........{item['quantity']}x {item['price']}")

# *****************************************************************************************************************

#                                          Another way to create dicts

# *****************************************************************************************************************

print("\nAnother way to create dict:")
person = dict(name="Bruno", age=32, country="Brazil")
print(person)

# *****************************************************************************************************************

#                                            ITERATING DICTIONARIES

# *****************************************************************************************************************

print("\nITERATING DICTIONARIES:")

# You can iterate over dictionaries using .values(), .keys() or .items() method

# .values() returns a list of all values
print("\nValues ->")
for value in person.values():
    print(value)

# .keys() returns a list of all keys
print("\nKeys ->")
for key in person.keys():
    print(key)

# .items() returns a list of tuples with keys and values
print("\nItems ->")
for key, value in person.items():
    print(f"{key}: {value}")

# *****************************************************************************************************************

#                                                           IN

# *****************************************************************************************************************

print("\nIN:")

# You can check if a key is in a dictionary using the "in" operator
course = {
    "name": "Introduction to Python",
    "idiom": "English",
    "duration": 40,
    "teacher": "Bruno",
    "language": "Python",
}
print(course)
print(f"\nThere is a 'name' key in course? {"name" in course}")
print(f"There is a 'Python' value in course? {'Python' in course.values()}")

# *****************************************************************************************************************

#                                                       CLEAR

# *****************************************************************************************************************

print("\nCLEAR:")
clear_me = {"name": "Bruno", "age": 32, "country": "Brazil"}

# You can empty a dictionary using clear
print(f"Before clear -> {clear_me}")
clear_me.clear()
print(f"After clear -> {clear_me}")

# *****************************************************************************************************************

#                                                      COPY

# *****************************************************************************************************************

print("\nCOPY:")

# You can copy a dictionary using copy
copied_course = course.copy()
print(f"Copied course -> {copied_course}")

# *****************************************************************************************************************

#                                                     FROMKEYS

# *****************************************************************************************************************

print("\nFROMKEYS:")

# You can create a key-value pair using fromkey
# For each value in the first argument, you create a key-value pair with the second argument
# PS: It works with strings, range, lists and tuples
print("\nCreate a key-value pair using fromkeys:")

fk = {}.fromkeys(["name"], "Vicente")
print(f"Creted a pair -> {fk}")

fk = {}.fromkeys(["name", "age", "country"], "unknown")
print(f"Created pairs -> {fk}")

# *****************************************************************************************************************

#                                                       GET

# *****************************************************************************************************************

print("\nGET:")

# You can get a value from a dictionary using get
# PS: If the key doesn't exist, it returns None
print(f"Course's dict -> {course}")
print(f"Name value -> {course.get('name')}")
print(f"Incorrect value -> {course.get('test')}")

# *****************************************************************************************************************

#                                                       POP

# *****************************************************************************************************************

print("\nPOP:")

# You can remove a key-value pair using pop
# PS: It returns the removed value. If the key doesn't exist, it returns an Error
print(f"Course before pop -> {course}")

print(f"\nRemoved duration -> {course.pop('duration')}")

print(f"\nCourse after pop -> {course}")


# *****************************************************************************************************************

#                                                    POPITEM

# *****************************************************************************************************************

print("\nPOPITEM:")

# You can remove a random key-value pair using popitem
print(f"Course before popitem -> {course}")
print(f"\nRemoved item -> {course.popitem()}")
print(f"\nCourse after popitem -> {course}")
