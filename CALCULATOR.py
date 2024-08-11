import math

def Calculator():
    # Function to perform basic arithmetic operations
    def Addition(x, y):
        return x + y

    def Subtraction(x, y):
        return x - y

    def Multiplication(x, y):
        return x * y

    def Division(x, y):
        if y == 0:
            return "Error! Division by zero."
        else:
            return x / y

    def Remainder(x, y):
        if y == 0:
            return "Error! Division by zero."
        else:
            return x % y

    def Square_Root(x):
        if x < 0:
            return "Error! Cannot take the square root of a negative number."
        else:
            return math.sqrt(x)

    def Exponent(x, y):
        return x ** y

    # Dictionary to map user input to function
    arithmetic_operations= {
        '1': Addition,
        '2': Subtraction,
        '3': Multiplication,
        '4': Division,
        '5': Remainder,
        '6': Square_Root,
        '7': Exponent
    }

    # Display the menu of operations
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Square Root")
    print("7. Exponent")

    # Get user input
    choice_preferred_by_user= input("Enter choice (1/2/3/4/5/6/7): ")

    if choice_preferred_by_user in arithmetic_operations:
        if choice_preferred_by_user == '6':
            try:
                input1 = float(input("Enter number: "))
                result = arithmetic_operations[choice_preferred_by_user](input1)
                print(f"The result is: {result}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            try:
                input1 = float(input("Enter first number: "))
                input2 = float(input("Enter second number: "))
                result = arithmetic_operations[choice_preferred_by_user](input1, input2)
                print(f"The result is: {result}")
            except ValueError:
                print("Invalid inputs. Please enter numeric values.")
    else:
        print("Invalid choice. Please select a valid operation.")

# Run the calculator
Calculator()
