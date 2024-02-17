import sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)