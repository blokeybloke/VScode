import sys
import random
from pyfiglet import Figlet

# Create a Figlet object
figlet = Figlet()

# Check the number of command-line arguments
if len(sys.argv) == 1:
    # If no arguments are provided, select a font randomly
    isRandomFont = True

elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    # If font is specified with -f or --font, use the specified font
    isRandomFont = False

else:
    # If arguments are invalid, print an error message and exit
    print("Invalid message")
    sys.exit(1)

# Retrieve the list of available fonts
figlet.getFonts()

# Set font based on user input or randomly
if isRandomFont == False:
    try:
        # Set the font to the one specified in the command line argument
        figlet.setFont(font=sys.argv[2])
    except:
        # If the specified font is invalid, print an error and exit
        print("Invalid usage")
        sys.exit(1)

else:
    # If random font is chosen, select a font randomly from available fonts
    font = random.choice(figlet.getFonts())

user = input("Input: ")

print("Output: ")
print(figlet.renderText(user))

# Alt version

import sys
import random
from pyfiglet import Figlet

# Function to check if a font is valid
def valid_font(font_name):
    return font_name in Figlet().getFonts()

# Initialize Figlet object
figlet = Figlet()

# Check command-line arguments
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    # Set the specified font if it's valid, otherwise exit
    if valid_font(sys.argv[2]):
        figlet.setFont(font=sys.argv[2])
    else:
        print("Invalid usage")
        sys.exit(1)

elif len(sys.argv) == 1:
    # Randomly choose a font
    figlet.setFont(font=random.choice(figlet.getFonts()))
else:
    # If arguments are not as expected, exit
    print("Invalid usage")
    sys.exit(1)


user_input = input("Input: ")

print("Output: ")
print(figlet.renderText(user_input))