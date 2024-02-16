import random

def main():
    level = get_level()
    score = games(level)
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x, y

def rounds(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

def games(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = rounds  (x,y)
        if response == True:
            score += 1
        count_round += 1
    return score
        
if __name__ == "__main__":
    main()

# Alt
import random

def main():
    # Get the difficulty level form user
    level = get_level()
    # Play the game at the specified level and get score
    score = play_games(level)
    # Print final score
    print("Score:", score)

def get_level():
    # Repeatedly prompt for level until valid one is entered
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level # Return the valid level
        except ValueError:
            # Inform user of invalid input and prompt again
            print("Please enter a valid level: 1, 2, or 3.")

def generate_random_numbers(level):
    # Generate pair of numbers based on level
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:   # level == 3
        return random.randint(100, 999), random.randint(100, 999)

def play_round(x, y):
    attempts = 0
    while attempts < 3:
        try:
            # Prompt user to solve math problem
            answer = int(input(f"{x} + {y} = "))
            if answer == x + y:
                return True # Correct answer
            else:
                print("EEE") # Incorrect answer, allow up to 3 attempts
        except ValueError:
            print("EEE")
        attempts += 1
    # Show the correct answer after 3 attempts
    print(f"{x} + {y} = {x + y}")
    return False

def play_games(level):
    total_score = 0
    for _ in range(10): # Play 10 games
        x, y = generate_random_numbers(level) # Get a math problem
        if play_round(x, y):
            total_score += 1 # Increment score for correct answers
    return total_score # Return the total score after all rounds

if __name__ == "__main__":
    main()
