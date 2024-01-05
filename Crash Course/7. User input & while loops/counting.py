# While loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Using continue in loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    # Omitting this line will cause infinite loop 
    x += 1

# Challenge - Pizza toppings
prompt = "What pizza toppings would you like? "
prompt += "\nEnter 'quit' when you are done: "

while True:
    pizza = input(prompt)
    if pizza == 'quit':
        break
    else:
        print(f"Adding {pizza} to your pizza!")
              
# Movie tickets
age = input("How old are you? ")
age = int(age)

while True:
    if age < 3:
        print("Your ticket is free!")
        break
    if age <= 12:
        print("The ticket is $10.")
        break
    else:
        print("Your ticket is $15.")
        break








