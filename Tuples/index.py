# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, dict-assign-update-to-union, while-to-for, for-index-replacement, remove-dict-keys
# *****************************************************************************************************************

#                                                    TUPLES

# *****************************************************************************************************************

# *****************************************************************************************************************

#                                                Tuple basics

# *****************************************************************************************************************

print("TUPLES:")

# Tuples are created with () or tuple()
nums = (1, 2, 3, 4, 5, 6, 5)
print(f"nums -> {nums}")

# You can access tuples with indexes
print(f"nums[0] -> {nums[0]}")

# Tuples are immutable
# nums[0] = 10 - > This will give you an error

# You can use in with tuples
print("5 is in nums: ", 5 in nums)

# To create a tuple with one value, you need to use a "comma" after the value
single_value_tuple = (5,)
print(f"single_value_tuple -> {single_value_tuple}")

# *****************************************************************************************************************

#                                              Tuple in dictionaries

# *****************************************************************************************************************

print("\nTUPLE IN DICTIONARIES:")

locations = {
    (35.6895, 39.6917): "Tokyo",
    (40.7128, 74.0060): "New York",
    (37.7749, 122.4194): "San Francisco",
}

print(f"locations -> {locations}")
print(f"\n(35.6895, 39.6917) -> {locations[35.6895, 39.6917]}")

# *****************************************************************************************************************

#                                             Loops with tuples

# *****************************************************************************************************************

print("\nLOOPS WITH TUPLES:")

for num in nums:
    print(num)

# *****************************************************************************************************************

#                                                 COUNT

# *****************************************************************************************************************

print("\nCOUNT:")

# You can count how many times a data appears in a tuple using count
print(f"The number 5 appears {nums.count(5)} times")

# *****************************************************************************************************************

#                                                 INDEX

# *****************************************************************************************************************

print("\nINDEX:")

# You can get the index of the first matching data in a tuple using index
print(f"The index of 5 is {nums.index(5)}")
