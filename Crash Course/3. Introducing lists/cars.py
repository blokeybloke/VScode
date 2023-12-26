# Alphabetical sort()
cars = ["bmw","audi", "toyota", "subaru"]
cars.sort()
print(cars)

# Reverse-alphabetical sort(reverse=True)
cars = ["bmw","audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

# Temporarily sorted()
cars = ["bmw","audi", "toyota", "subaru"]
print("Here is the orignal list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Reverse order
cars = ["bmw","audi", "toyota", "subaru"]
cars.reverse()
print(cars)

# Challenge - Seeing the world
world = ["japan", "south korea", "switzerland", "germany", "prague"]
print(world)

print(sorted(world))
print(world)

world.reverse()
print(world)

world.reverse()
print(world)

world.sort()
print(world)

world.sort(reverse=True)
print(world)
