"""Project 6: Lambda Function Calculator (Concepts: Lambda Functions)
Purpose: Implement a simple calculator using lambda functions.

Key concepts: Lambda functions, functional programming.

Use cases: Basic operations like addition, subtraction, multiplication, and division using lambda.
"""

def Calculator(a, b, choice):
    if choice == 1:
        x = lambda a, b: a + b
        print(x(a, b))
    elif choice == 2:
        x = lambda a, b: a - b
        print(x(a, b))
    elif choice == 3:
        x = lambda a, b: a * b
        print(x(a, b))
    elif choice == 4:
        x = lambda a, b: a // b
        print(x(a, b))
    else:
        print("Invalid Response")


a = int(input("Enter the your first number "))
b = int(input("Enter your second number "))
choice = int(input("Enter your operation(1.add/2.subtract/3.multiply/4.divide)"))
Calculator(a, b, choice)
