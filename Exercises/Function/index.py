# Create a Function that returns a list of all the even number from 0 to 50,
# excluding 50:


def generate_evens():

    arr = []
    [arr.append(n) if n % 2 == 0 else n for n in range(1, 50)]

    return arr


print("\nEven numbers from 0 to 50:")
print(generate_evens())
