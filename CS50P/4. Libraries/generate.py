# Import random module
import random

coin = random.choice(["heads", "tails"])
print(coin)

# Alternative
from random import choice

coin = choice(["heads", "tails"])
print(coin)

# Random int
import random

number = random.randint(1, 10)
print(number)

# shuffle
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)