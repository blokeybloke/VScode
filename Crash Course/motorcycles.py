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

# Challenge - Guest list
guests = ["Candace Owens", "Joe Rogan", "Charlie Munger"]
print(f"Hi {guests[0]}, would you like to come to dinner?")
print(f"Hi {guests[1]}, would you like to come to dinner?")
print(f"Hi {guests[2]}, would you like to come to dinner?")
# Changing guest list
cannot_attend = guests.pop()
print(f"{cannot_attend}, can no longer attend dinner.")

guests.append("Elon Musk")
print(f"Hi {guests[0]}, would you like to come to dinner?")
print(f"Hi {guests[1]}, would you like to come to dinner?")
print(f"Hi {guests[2]}, would you like to come to dinner?")
# More guests
print("I have found a bigger table and will be inviting 3 more guests.")
guests.insert(0, "Mike Tyson")
guests.insert(2, "Michael Jackson")
guests.append ("Donald Trump")
print(guests)
#Shrinking guest list
new_guests = ['Mike Tyson', 'Candace Owens', 'Michael Jackson', 'Joe Rogan', 'Elon Musk', 'Donald Trump']
print(new_guests)
kicked = new_guests.pop()
print(f"Sorry {kicked} you have been kicked out.")
print(new_guests)
kicked = new_guests.pop()
print(f"Sorry {kicked} you have been kicked out.")
print(new_guests)
kicked = new_guests.pop()
print(f"Sorry {kicked} you have been kicked out.")
print(new_guests)
kicked = new_guests.pop()
print(f"Sorry {kicked} you have been kicked out.")
print(new_guests)

print(f"Hi {new_guests[0]}, you are still invited.")
print(f"Hi {new_guests[1]}, you are still invited.")

del new_guests[0]
del new_guests[0]
print(new_guests)