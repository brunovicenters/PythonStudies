for item in range(1, 21):
    if item == 4 or item == 13:
        state = "unlucky"
    elif item % 2 == 0:
        state = "even"
    else:
        state = "odd"

    print(f"{item} is {state}.")
