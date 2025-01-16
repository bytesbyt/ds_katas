## simulate rolling a dice

import random

def dice_roll():
    while True:
        try:
            # set the min and max number that your dice can produce
            min = int(input("What is the min number that dice can produce? Please enter an integer: "))
            max = int(input("What is the max number that dice can produce? Please enter an integer: "))

            if min >= max:
                print("The mininum value must be less than the max value. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter an integer number.")
 
    
    while True:
        # Asks if you'd like to roll again
        roll = input("Do you want to roll the dice? (y/n): ").lower()
        if roll == 'y':
            # randomly choose a number bewtween min and max numbers and print the number
            print(random.randint(min, max))
            continue
        elif roll == 'n':
            print("Good bye! Thanks for playing.")
            break
        else:
            print("Invalid Input. Please enter 'y' or 'n'.")
    
dice_roll()
