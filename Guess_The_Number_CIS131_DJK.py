# File Name: Guess The Number - CIS131
# Description: This program is a number guessing game where the player guesses a randomly chosen integer (1-1000).
# Author: Dakota Kartchner 
# Date Created: 1/29/2025

import random

while True:
    number_to_guess = random.randint(1, 1000)  # Generate a random number between 1 and 1000
    attempts = 0  # Initialize the attempt counter

    print("Guess my number between 1 and 1000 with the fewest guesses:")

    while True:
        try:
            guess = int(input("Enter your guess: "))  # Get users guess
            attempts += 1  # Add one attempt to counter

            if guess < number_to_guess:
                print("Too low. Try again.")
            elif guess > number_to_guess:
                print("Too high. Try again.")
            else:
                print("Congratulations! You guessed the number in " + str(attempts) + "attempts.")
                if attempts <= 10:
                    print("Either you know the secret or you got lucky!")
                else:
                    print("You should be able to do better!")
                break  # Exit the loop when the number is guessed correctly
        except ValueError:
            print("Invalid input. Please enter a number.")

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break  # Exit the game loop
