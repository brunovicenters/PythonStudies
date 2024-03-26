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
