# Import random module to generate random numbers
import random

# Prompt the user for a level until a valid positive integer is entered
while True:
    try:
        # Convert user input to integer
        user = int(input("Level: "))
        # If conversion sucessfull and positive number, exit loop
        if user >0:
            break
    except ValueError:
        # If input is not an integer, siletly ignore and retry
        pass

# Generate random number between 1 and user input
random_numb = random.randint(1, user)

# Main guessing loop: prompt the user to guess number until correct
while True:
    try:
        guess = int(input("Guess: "))
        # If guess not positive, inform user it's too small
        if guess <= 0:
            print("Too small!")
        # If guess less than random number, inform user it's too small
        elif guess < random_numb:
            print("Too small!")
        # If guess greater than random number, inform user it's too large
        elif guess > random_numb:
            print("Too large!")
        # If none of the above conditions are true, guess must be correct
        else:
            print("Just right!")
            break   # Exit loop as user has guessed correct number.
    except ValueError:
        pass



