alien_0 = {"colour": "green", "points": 5}

print(alien_0["colour"])
print(alien_0["points"])

# new points
new_points = alien_0["points"]
print(f"\nYou have earned {new_points} points!")

# adding new key values
alien_0 = {"colour": "green", "points": 5}
print(alien_0)

alien_0["x_postion"] = 0
alien_0["y-position"] = 25
print(alien_0)

# empty dictionary
alien_0 = {}

alien_0["colour"] = "green"
alien_0["points"] = 5

print(alien_0)

# Modifying value in dictionary

alien_0 = {"colour": "green"}
print(f"Alien was {alien_0['colour']}.")

alien_0["colour"] = "yellow"
print(f"Now the alien is {alien_0['colour']}")

alien_0 = {"x_postion": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_postion']}")

# Move alien to the right
# Determine how far to move the alien based on its current speed

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

# New position = old position + increment
alien_0["x_postion"] = alien_0["x_postion"] + x_increment

print(f"New position: {alien_0['x_postion']}")

# Turn into fast alien
alien_0["speed"] = "fast"

# Removing key points
alien_0 = {"colour": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

# get() to access values
alien_0 = {"colour": "green", "speed": "slow"}
point_value = alien_0.get("points", "No point value assigned.")
print(point_value)

# Nesting a list of dicts
alien_0 = {"colour" : "green", "points" : 5}
alien_1 = {"colour" : "yellow", "points" : 10}
alien_2 = {"colour" : "red", "points" : 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Empty list for storing aliens
aliens = []

for alien_number in range(30):
    new_alien = {"colour" : "green", "points" : 5, "speed" : "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["colour"] == "green":
        alien["colour"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["colour"] == "yellow":
        alien["colour"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

for alien in aliens[:5]:
    print(aliens)
print("...")

print(f"Total number of aliens: {len(aliens)}")