# This program is used to act like a real random throw of a dice
import random  # Allows the use of a random number generator

minimum = 1  # Sets the lowest number of the dice. It will obviously always be 1

#  This allows the user to choose the side of the dice assuming it will have at least
#  two sides. It will tell them off if they try and be sneaky and pick less.

while True:
    try:
        maximum = (int(input("How many sides does your dice have? ")))
    except ValueError:  # This prevents the user entering a blank space or a string
        print("I'm sorry you have to enter a number or press CTRL + F2 to exit")
        continue
    if maximum <= 2:
        print("""Nice try! Your dice must have at least two sides obviously.
              Please give a sensible answer or press CTRL + F2 to exit""")
        continue
    else:
        break

print("""So you want to play a game? how many dice rolls do you need?
 ... BUT NO MORE THAN 5 or I close the program!""")

# This block sets a value for loops as long as it is more than 0, not exactly 0 and the user doesn't attempt to enter a string.

while True:
    try:
        loops = (int(input("Enter amount here: ")))
    except ValueError:
        print("I'm sorry you have to enter a number or press CTRL + F2 to exit")
        continue
    if loops < 0:
        print("Now come on pick a positive number! or press CTRL + F2 to exit ")
        continue
    elif loops == 0:
        print("If you didn't want to roll the dice you could of just said! Try again or press CTRL + F2 to exit")
        continue
    else:
        break

# This block provides the randomly generated number for the dice as long as they picked 5 or less in the above.
# Otherwise as they are told at the beginning, the program closes.
        
for roll in range(loops):
    if loops <= 5:
        result = random.randint(minimum, maximum)  # Sets result to be a random number between 1 and the user entered maximum.
        print(result)
    elif loops > 5:
        print("Hey we both know I said less than 5!")
        exit()



