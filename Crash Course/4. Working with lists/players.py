# Slicing a list
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

# 2
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:4])

# omit first index in slice
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[:4])

# omitting the 2nd index
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[2:])

# print last the items
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[-3:])

# slice with for loop
players = ["charles", "martina", "michael", "florence", "eli"]

print("Here are the first 3 players on my team:")
for player in players[:3]:
    print(player.title())

# Challenge - Slices
exercies = ["squat", "bench", "overhead", "pull-up", "deadlift"]
print("The first 3 exercises in this list are:")
print(exercies[0:3])

print("The middle 3 exercises in this list are:")
print(exercies[1:4])

print("The last 3 exercises in this list are:")
print(exercies[-3:])