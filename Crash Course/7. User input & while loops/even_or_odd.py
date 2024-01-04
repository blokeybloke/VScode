# Modulo operator divides number by number and returns remainder
number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")

else:
    print(f"\nThe number {number} is odd.")

# Challenge - Rental car
message = input("What kind if car would you like? ")
print(f"\nLet me see if I can find you a {message}.")

# Seating
dinner = input("How many people are seating? ")
dinner = int(dinner)

if dinner >8:
    print("Please wait for a table.")

else:
    print("Your table is ready.")

# Multiples of ten
multiples = input("Please enter a number: ")
multiples = int(multiples)

if multiples % 10 == 0:
    print(f"{multiples} is a multiple of 10.")
else:
    print(f"{multiples} is not a multiple of 10.")