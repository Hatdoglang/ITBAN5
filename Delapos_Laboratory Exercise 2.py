# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:57:48 2024

@author: Christian Delapos D.
"""

# Function to perform the arithmetic operation based on user choice
def perform_operation(number1, number2, choice):
    # Addition
    if choice == '1':
        result = int(number1 + number2)
        operator = '+'
    # Subtraction
    elif choice == '2':
        result = int(number1 - number2)
        operator = '-'
    # Multiplication
    elif choice == '3':
        result = int(number1 * number2)
        operator = 'x'
    # Division
    elif choice == '4':
        # Check for division by zero
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
            return None, None
        result = number1 / number2
        operator = '/'
    else:
        print("Invalid choice")
        return None, None

    return result, operator

# Main program loop
while True:
    # Ask the user to choose an operation
    print("-------------------------------------------------")
    print("Choose an operation:")
    print("-------------------------------------------------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (x)")
    print("4. Division (/)")
    print("-------------------------------------------------")

    # Take input for the operation choice
    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")

    # Take input from the user for two numbers
    while True:
        try:
            print("-------------------------------------------------")
            number1 = int(input("Enter the first number: ")) if choice in ['1', '2', '3'] else float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            print("-------------------------------------------------")
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    # Perform the chosen operation
    result, operator = perform_operation(number1, number2, choice)

    # Check if result is not None (i.e., operation was valid)
    if result is not None:
        # Print the result of the operation
        print("-------------------------------------------------")
        if choice == '4':
            print(f"The result of {number1} {operator} {number2} = {result}")
        else:
            print(f"The result of {number1} {operator} {number2} = {int(result)}")
        print("-------------------------------------------------")

    # Ask the user if they want to continue
    continue_input = input("Type 'yes' to continue or 'no' to exit: ")
    if continue_input.lower() != 'yes':
        break
