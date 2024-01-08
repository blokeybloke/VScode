places = []
# Step 1: Ask for the user's favorite places
user = input("What are your favourite places? ")
places.append(user)
user = input("What is your 2nd favourite place? ")
places.append(user)
user = input("What is your 3rd favourite place? ")
places.append(user)
# Step 2: Sort and display the list alphabetically
sorted_list = sorted(places)
print(sorted_list)
# Step 3: Display the list in reverse alphabetical order
reverse = sorted(places, reverse=True)
print(reverse)
# Step 4: Show the original list is unchanged
print(places)
# Step 5: Reverse the original list and display it
places.reverse()
print(places)