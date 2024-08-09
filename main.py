print("Welcome to the calcular program!")

first_number = int(input("Please enter the first number "))
second_number = int(input("Please enter the second number "))

operation = input("Please enter the operation you want to execute ")

if operation == "+":
    print(f"The addition of the numbers is {first_number + second_number}")

elif operation == "-":
    print(f"The subtraction of the numbers is {first_number - second_number}")

elif operation == "*":
    print(f"The multiplication of the numbers is {first_number * second_number}")

elif operation == "/":
    print(f"The division of the numbers is {first_number / second_number}")
          
else:
    print(f"Unknown operation")