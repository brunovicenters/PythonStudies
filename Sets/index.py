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
