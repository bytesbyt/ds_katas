# import python random module
import random

def number_guess():
    # first randomly generate a number unknown to the user.
    random_number = random.randint(1,100)

    while True:
        try:
            # The user needs to guess what that number is.
            guess = int(input("Guess the number between 1 and 100: "))
            # If the user guesses correctly, a positive indication should appear.
            if guess == random_number:
                print("Congratulations! You have guessed the number correctly!")
                break
            # If the user’s guess is wrong, the program should return some sort of indication as to how wrong
            elif guess > random_number:
                print("The number you have guessed is too high! Please try again.")
            else:
                print("The number you have guessed is too low! Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number")
        
number_guess()