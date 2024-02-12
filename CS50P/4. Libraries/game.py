import random

while True:
    try:
        user = int(input("Level: "))
        n = user
        number = random.randint(1, n)
        
        
    except ValueError:
        print(user)



#n = user
#number = random.randint(1, n)

#print(user)