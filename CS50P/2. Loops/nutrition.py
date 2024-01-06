fruit = {
    "apple": 130,
    "avocado": 50,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100
}

item = input("Item: ").lower()

if item in fruit:
    print(f"Calories: {fruit[item]}")