# Simple calculator that performs the 4 operations


# Store allowed symbols in 'symbols'
symbols = [" ", ".", "+", "-", "*", "/"]

print("\nEnter '0' to end the script.")

# Continuously loop the calculator
while True:

    # Get math equation and store it in 'equation'
    equation = input("\nEnter your equation in the format (x + y / z...): ")

    # End script
    if equation == "0":
        print("\nEnding script...")
        exit(0)

    # Sanitise 'equation'
    for i in equation:
        if not i.isdigit():
            if i not in symbols:
                valid = False
                break
            valid = True
        valid = True
    if not valid:
        print("Equation is invalid.")

    # Calculate result of equation
    else:
        result = f"{eval(equation):,}"
        print(f"Result: {result}")
