from calculator import add, subtract, multiply, divide

def main():
    print("Welcome to the Python Calculator! Type 'exit' to quit.")

    while True:
        # Read input
        user_input = input("Enter operation and two numbers (e.g., add 5 3): ")

        # Exit condition
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        # Parse input
        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)
        except ValueError:
            print("Invalid input. Use format: <operation> <num1> <num2>")
            continue

        # Evaluate
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                continue
        else:
            print(f"Unknown operation '{operation}'. Supported: add, subtract, multiply, divide.")
            continue

        # Print result
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
