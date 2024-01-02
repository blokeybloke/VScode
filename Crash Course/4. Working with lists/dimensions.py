# Tuple is unchangable/immutable list
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# For loop in dimensions
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Redfine entire tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Challenge - buffet
buffets = ("sashimi", "oyster", "wagyu", "pizza", "pasta")
for buffet in buffets:
    print(buffet)

buffets = ("sashimi", "oyster", "wagyu", "pizza", "pasta")
print("Old buffet:")
for buffet in buffets:
    print(buffet)

buffets = ("tuna", "oyster", "wagyu", "pizza", "pasta")
print("\nNew buffet:")
for buffet in buffets:
    print(buffet)