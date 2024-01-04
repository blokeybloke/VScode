message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# while loop with quit value
prompt = "\nTell me something and I'll reapeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)