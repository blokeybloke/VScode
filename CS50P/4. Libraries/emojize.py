# Import emoji module
import emoji
# Prompt user
user = input("Input: ")
# Convert emoji aliases in user input to actual emojis
emoji = emoji.emojize(user, language="alias")

print("Output: ", emoji)