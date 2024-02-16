import random

while True:
    try:
        user = int(input("Level: "))
        if user >0:
            break
    except ValueError:
        pass

random_numb = random.randint(1, user)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            print("Too small!")
        elif guess < random_numb:
            print("Too small!")
        elif guess > random_numb:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass



