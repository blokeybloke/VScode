# Check for inequality
requested_toppings = "mushrooms"

if requested_toppings != "anchovies":
    print("Hold the anchovies!")

# Test multiple conditions
requested_toppings1 = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings1:
    print("Adding mushroom")
if "pepperoni" in requested_toppings1:
    print("Adding pepperoni")
if "extra cheese" in requested_toppings1:
    print("Adding extra cheese")

print(f"\nFinished making your pizza!")

# Challenge - Alien colour
alien = ["yellow"]
if "red" in alien:
    print(f"Alien is red, you have earned 5 points")

elif "yellow" in alien:
    print(f"You have earned 7.5 points.")

else:
    print(f"You have earned 10 points!")

# Challenge - Stages of life
age = 69
if age <2:
    print("You are a baby!")
elif age <4:
    print("You are a toddler!")
elif age <13:
    print("You are a kid!")
elif age <20:
    print("You are a teenager!")
elif age <65:
    print("You are an adult!")
else:
    print("You are and elder!")

# Challenge - Favourite fruits
favourite_fruit = ["mango", "orange", "strawberry", "apple", "kiwi"]
if "mango" in favourite_fruit:
    print(f"I really love {favourite_fruit[0]}!")

# For loop with list
toppings = ["mushrooms", "green peppers", "extra cheese"]
for topping in toppings:
    if topping == "green peppers":
        print("Sorry we are out of green peppers right now.")

    else:
        print(f"Adding {topping}.")

print("\nFinished making your pizza!")

# Will print else if list empty
toppings = []
if toppings:
    for topping in toppings:
        print(f"Adding {topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a free pizza?")

# Multiple lists
availables = ["ham", "cheese", "tomato", "onion", "pepperoni", "chicken"]

requesteds = ["pepperoni", "oregano", "cheese"]

for requested in requesteds:
    if requested in availables:
        print(f"Adding {requested}")
    else:
        print(f"Sorry we don't have {requested}.")

print("\nFinished making your pizza!")

# Challenge - Hello admin
usernames = ["admin", "user", "vien", "bloke", "fiona"]

login = input("What is your login name? ")

for user in usernames:
    if user == "admin" and login == "admin":
        print(f"Hello {user}, would you like to see the status report?")
        break
    elif user == "vien" and login == "vien":
        print(f"Hello {user}, welcome back.")
        break
    else:
        print("Invalid login name. Please check your username.")

# Challenge - no user
users = []
if "vien" in users:
    print("Hello Vien!")
else:
    print("We need more users!") 

# Challenge - checking usernames
current_users = ["admin", "user", "vien", "bloke", "fiona"]

new_users = ["VIEN", "fiona", "new", "newuser", "adminstrator"]

for new in new_users:
    if new in current_users:
        print("Sorry this username is taken. Please try again")

    else:
        print("Username is available")

# Challenge - ordinal numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")

    elif number == 2:
        print(f"{number}nd")

    elif number == 3:
        print(f"{number}rd")

    elif number == 4:
        print(f"{number}th")

    elif number == 5:
        print(f"{number}th")

    elif number == 6:
        print(f"{number}th")

    elif number == 7:
        print(f"{number}th")

    elif number == 8:
        print(f"{number}th")

    else:
        print(f"{number}th")