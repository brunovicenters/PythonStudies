# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, while-to-for, for-index-replacement, remove-dict-keys
print("Exercises:")

# DICT ITERATION -->
print("\nDICT ITERATION -->")

# Get the total of donations in the dict
donations = dict(
    sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0
)
total_donations = 0
for donation in donations.values():
    total_donations += donation
print(f"Total donations: {total_donations}")

# DICT COMPREHENSION -->
print("\nDICT ITERATION -->")

# Given two lists, create a dict with the first list as keys and the second as values
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(len(list1))}
print(answer)

# Given a list with lists, create a dict where the first item is the key and the second is the value
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

answer = {
    person[i][0]: person[i][1] for i in range(len(person))
}  # or answer = dict(person)
print(f"\n{answer}")

# Make the correspondig letter to it ASCII code from 65 to 90
answer = {i: chr(i) for i in range(65, 91)}
print(f"\n{answer}")
