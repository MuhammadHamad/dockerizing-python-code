import math

def get_number(prompt):
    """Prompts the user for a number, ensuring it's a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def exponentiate(x, y):
    return math.pow(x, y)

def perform_operation(first_number, second_number, operation):
    """Performs the specified arithmetic operation."""
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "^": exponentiate
    }
    func = operations.get(operation)
    if func:
        return func(first_number, second_number)
    else:
        return "Error: Unknown operation."

def main():
    """Main function for the calculator program."""
    print("Welcome to the calculator!")

    while True:
        first_number = get_number("Please enter the first number: ")
        second_number = get_number("Please enter the second number: ")

        print("Available operations:")
        print("+: Addition")
        print("-: Subtraction")
        print("*: Multiplication")
        print("/: Division")
        print("^: Exponentiation")

        operation = input("Please enter the operation you want to execute: ")

        result = perform_operation(first_number, second_number, operation)
        print(f"The result is: {result}")

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    main()