# Challenge
car = "subaru"
print("Is car == 'subaru' ? I predict True.")
print(car == 'subaru')

print("\nIs car == to 'audi' ? I predict False.")
print(car == 'audi')

if car != "audi":
    print(f"Not a {car.title()}!")

jap_car = "mazda"
if jap_car not in car:
    print(f"Not the same car!")