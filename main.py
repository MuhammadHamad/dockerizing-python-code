def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def perform_operation(first_number, second_number, operation):
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
    else:
        return "Unknown operation."

def main():
    print("Welcome to the calculator program!")

    first_number = get_number("Please enter the first number: ")
    second_number = get_number("Please enter the second number: ")

    operation = input("Please enter the operation you want to execute (+, -, *, /): ")

    result = perform_operation(first_number, second_number, operation)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()