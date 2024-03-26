# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, while-to-for;for-index-replacement
# *****************************************************************************************************************

#                                                    DICTIONARY

# *****************************************************************************************************************

# *****************************************************************************************************************

#                                            How to a create a dictionary

# *****************************************************************************************************************

print("\nDICTIONARY:")

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

#                                           Another way to create dict

# *****************************************************************************************************************

print("\nAnother way to create dict:")
person = dict(name="Bruno", age=32, country="Brazil")
print(person)
