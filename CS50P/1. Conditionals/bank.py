# User input
name = input ("Greetings: ").strip()
# Wrong greeting gives $100
if name == "Hello" or name == "Hello, Newman":
    print("$0")
elif name == "How you doing?":
    print("$20")
else:
    print("$100")