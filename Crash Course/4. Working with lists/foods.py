# Copying a list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

# Proving 2 separate lists by adding item
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("canoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

# Challenge - my pizza, your pizza
pizzas = ["pepperoni", "cheesy", "garlic"]
friends_pizza = ["pepperoni", "cheesy", "garlic"]

pizzas.append("meatlovers")
friends_pizza.append("vegetarian")

print("My favorite pizza are:")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are:")
for friend in friends_pizza:
    print(friend)