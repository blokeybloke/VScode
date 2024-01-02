# for loop to print list
magicians = ["alice", "david", "carloina"]
for magician in magicians:
    print(magician)

# for loop with a message
magicians = ["alice", "david", "carloina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
# printing outside of for loop
print("Thank you everyone, that was great show!")

# forgetting to indent
magicians = ["alice", "david", "carloina"]
for magician in magicians:
#print(magician)

#for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Challenge - Pizza
pizzas = ["pepperoni", "garlic", "cheesy"]
for pizza in pizzas:
    print(f"I love {pizza} pizza!")
print("\nI love all pizzas!")

animals = ["cat", "dog", "wolf"]
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("\nThey would all make great pets.")

