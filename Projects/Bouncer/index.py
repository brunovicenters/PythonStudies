age = input("How old are you: ")

if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")
    elif age >= 21:
        print("You're good to enter and drink!")
    else:
        print("You can't enter!")
else:
    print("You didn't enter an age!")
