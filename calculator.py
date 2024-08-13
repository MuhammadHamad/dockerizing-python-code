import math

def get_number(prompt):
    """Prompts the user for a number, ensuring it's a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def perform_operation(first_number, second_number, operation):
    """Performs the specified arithmetic operation."""
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number == 0:
            return "Error: Division by zero is not allowed."
        return first_number / second_number
    elif operation == "^":
        return math.pow(first_number, second_number)
    else:
        return "Unknown operation."

def main():
    """Main function for the calculator program."""
    print("Welcome to the enhanced calculator!")

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
