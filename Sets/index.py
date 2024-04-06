# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, dict-assign-update-to-union, while-to-for, for-index-replacement, remove-dict-keys, unwrap-iterable-construction, remove-duplicate-set-key;
# *****************************************************************************************************************

#                                                  SETS

# *****************************************************************************************************************

# *****************************************************************************************************************

#                                               Sets basics

# *****************************************************************************************************************

print("SETS:")

# Sets do not have duplicated data and they are unordered

# To create a set, use set() or {}
s = set({1, 2, 3, 4, 4, 5, 5, "a", "b", 3.982})
print(s)

# You cannot access a set with indexes
# s[0] - > This will give you an error

# You can use in with sets
print("5 is in s: ", 5 in s)

# *****************************************************************************************************************

#                                             Loops with sets

# *****************************************************************************************************************

print("\nLOOPS WITH SETS:")

for item in s:
    print(item)

# *****************************************************************************************************************

#                                                ADD

# *****************************************************************************************************************

print("\nADD:")

# You can add items to a set using .add()
s.add("Tarsila")
print(s)

# But you can't add items that are already in the set
s.add(5)
print(f"Trying to add 5 again -> \n{s}")

# *****************************************************************************************************************

#                                                REMOVE

# *****************************************************************************************************************

print("\nREMOVE:")

print(f"Before remove -> \n{s}")
# You can remove items from a set using .remove()
s.remove(4)
print(f"After remove -> \n{s}")

# If you try to remove an item that doesn't exist, it will raise an error
# s.remove(4) -> This will raise an error


# *****************************************************************************************************************

#                                              DISCARD

# *****************************************************************************************************************

print("\nDISCARD:")

print(f"Before discard -> \n{s}")

# Just like remove, you can discard items from a set using .discard()
# But it doesn't raise an error if the item doesn't exist
s.discard(4)
print(f"After discarding '4' -> \n{s}")
s.discard(1)
print(f"After discarding '1' -> \n{s}")
