# Modify 1st element in list to Ducati
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)

motorcycles[0] = "Ducati"
print(motorcycles)

# Adding element to list
motorcycles.append ("BMW")
print(motorcycles)

# Adding to empty list
motorcycles = []
motorcycles.append ("BMW")
motorcycles.append ("Ducati")
motorcycles.append ("Yamaha")
motorcycles.append ("Suzuki")
print(motorcycles)

# Insert into list
motorcycles = ["Honda", "Yamaha", "Suzuki"]
motorcycles.insert(2, "Ducati")
print(motorcycles) 

# Delete element in list
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Remove last item using pop()
motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)

popper_motorcycle = motorcycles.pop()
print(motorcycles)
print(popper_motorcycle)

# Using pop() in sentence
motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print(f"The last bike I bought was a {last_owned.title()}.")

# pop() any item from list
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(1)
print(f"The first bike I owned was a {first_owned.title()}.")

# Remove item by value
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.remove("yamaha")
print(motorcycles)

# Remove item by value and reason
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

too_gay = "suzuki"
motorcycles.remove(too_gay)
print(motorcycles)
print(f"\nA {too_gay.title()} is too gay for me.")

# Challenge - 