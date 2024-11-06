# Ask the user for their desired travel distance
distance = float(input("How far would you like to travel in miles? "))

# Determine the recommended mode of travel based on distance
if distance < 3:
    print("I suggest walking to your destination.")
elif distance < 300:
    print("I suggest driving to your destination.")
else:
    print("I suggest flying to your destination.")
