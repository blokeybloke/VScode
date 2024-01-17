menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
# Variable to keep track of running total
running_total = 0
# Start loop to ask for user input
while True:
    try:
        food = input("Item: ").title()

    except EOFError:
        break

    if food in menu:
        running_total += menu[food]
        # Print value formatted as a dollar amount
        print(f"Total: ${running_total:.2f}")

