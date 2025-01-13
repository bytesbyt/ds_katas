## simulate rolling a dice
# randomly choose a number bewtween 1 and 6 and print the number

# Asks if you'd like to roll again

# set the min and max number that your dice can produce

import random
def dice_roll():
    min = input("What is the min number that dice can produce? Please enter an integer:")
    max = input("What is the max number that dice can produce? Please enter an integer:")
    random.randint(min, max)

dice_roll()
