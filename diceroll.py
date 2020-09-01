import random
reroll = "y"

# Dice Ascii Lines
zero = "|       |"
odd = "|   O   |"
even = "| O   O |"
trip = "| O O O |"

# Dice Ascii Print Function
def print_dice(line1, line2, line3):
    print("---------") 
    print(line1) 
    print(line2) 
    print(line3) 
    print("---------")

# Dice Result Dictionary
dice_img = {
    1 : [zero, odd, zero],
    2 : [zero, even, zero],
    3 : [odd, odd, odd],
    4 : [even, zero, even],
    5 : [even, odd, even],
    6 : [even, even, even],
    7 : [even, trip, even],
    8 : [trip, even, trip],
    9 : [trip, trip, trip],
}

# Dice Roll Main Code
while reroll == "y":
    min = 1
    max = int(input("number of sides?"))
    num_of_rolls = int(input("number of dice?"))
    results = []
    x = 1

    while x <= num_of_rolls:
        diceroll = random.randint(min, max)
        x += 1

        #Dice Result with Ascii
        if max <= 9:
            print_dice(*dice_img[diceroll])
        
        #Dice Result without Ascii
        else: 
            print(diceroll)

        results.append(diceroll)

    print("Total dice roll is: %d!" %(sum(results)))
    
    # Continue or end statement
    reroll = input("Would you like to reroll? y or n...")
    if reroll == "n":
        reroll = "n"
else:
    print("Goodbye")

