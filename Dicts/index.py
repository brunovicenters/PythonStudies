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
