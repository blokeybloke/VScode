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