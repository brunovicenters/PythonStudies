# Given an unsorted array of integers, find the length of the longest consecutive
# elements sequence.

# For example, Given [100, 4, 200, 1, 3, 2], The longest consecutive elements
# sequence is [1, 2, 3, 4]. Return its length: 4.

first_arr = [100, 4, 200, 1, 3, 2]

second_arr = [0, 3, 7, 2, 5, 8, 4, 6, 1, 9]


def longest_consecutive_sequence(nums) -> int:

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:

        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


print(f"The longest consecutive sequence in {first_arr} is:")
print(longest_consecutive_sequence(first_arr))

print(f"\nThe longest consecutive sequence in {second_arr} is:")
print(longest_consecutive_sequence(second_arr))
