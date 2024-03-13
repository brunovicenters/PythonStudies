age = input("How old are you: ")

if age:
    age = int(age)
    if age >= 21:
        print("You're good to enter and drink!")
    elif age >= 18:
        print("You can enter, but need a wristband!")
    else:
        print("You can't enter!")
else:
    print("You didn't enter an age!")
