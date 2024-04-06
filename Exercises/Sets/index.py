# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, dict-assign-update-to-union, while-to-for, for-index-replacement, remove-dict-keys, unwrap-iterable-construction, remove-duplicate-set-key;
# *****************************************************************************************************************

#                                                  SETS

# *****************************************************************************************************************

# Get rid of duplicates
cities = ["Berlin", "Hamburg", "Berlin", "Frankfurt", "Munich", "Berlin", "Hamburg"]
results = set(cities)
print(results)
