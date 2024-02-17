import sys # Import sys module to access command-line arguments
import requests # Import the requests module to make HTTP requests

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1) # Exit with error code

# Try to convert the command-line argument to a float
try:
    value = float(sys.argv[1]) # Attempt to convert the 2nd command-line argument to a float
except ValueError: # Catch the exception if conversion fails
    print("Command-line is not a number")
    sys.exit(1) # Exir program with error code

# Try to get current Bitcoin price from CoinDesk API
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json() # HTTP GET request and parse the JSON response
    bitcoin = response["bpi"]["USD"]["rate_float"] # Extract current price in USD
    total_amount = bitcoin * value # Calculate total value based on user input
    print(f"${total_amount:,.4f}") # Print calculated total formatted as currency

except requests.RequestException: # Catch request-related exceptions
    print("RequestException")
    sys.exit(1)
