total = 50
# Continue loop until 0 or less
while total > 0:
    print("Amount due:", total)
    user = int(input("Insert coin: "))
    # Check if coin is an accepted denomination
    if user in [5, 10, 25]:
        total -= user
        
change = abs(total)

print("Change owed:", change)