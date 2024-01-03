# Check whether value is NOT in list
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Check whether value is IN list
banned_users = ["andrew", "carolina", "david"]
user = "andrew"
if user in banned_users:
    print(f"{user.title()}, you cannot post.")