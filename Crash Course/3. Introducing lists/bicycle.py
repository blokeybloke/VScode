# Square brackets [] represent a list
bicycles = ["trek", "cannondale", "redline", "specialised"]

# print [0] first item and capitalising
print(bicycles[0].title())

# print 2nd and 4th item. Python will -1
print(bicycles[1])
print(bicycles[3])

# -1 will print last item in list
print(bicycles[-1])

# Use individual valur from list with f-string
message = f"My first bike was a {bicycles[0].title()}"
print(message)

# Challenge - Names
names = ["Vien", "Fiona", "Kora"]
print(names[0])
print(names[1])
print(names[2])

# Challange - Greetings
greetings = f"Merry Christmas, {names[0]}!"
print(greetings)

# Challenge - Own list
cars = ["VW Golf R", "Mercedes CLA45s", "Audi RS3"]
dream = f"I would like own a {cars[-1]} one day..."
print(dream)