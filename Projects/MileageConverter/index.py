# THIS PROJECT WILL CONVERT KILOMETERS TO MILES

# Defining conversion km to mile --
KM_TO_MILE = 1.60934

# Asking user input --
print("How many kilometers did you run today?")
km = float(input())

# Converting km to mile --
miles = round(km/KM_TO_MILE, 2)

# Printing result --
print(f"Your {km}km run was {miles}mi")