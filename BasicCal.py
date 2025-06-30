"""In this calculator we have function calculator which is expect only integer value if any other
if raises a valueerror and provide various function like sum ,difference multiply , divide and more..
Also handled input errors.
"""


def calculator():
    try:
        num1 = (int(input("Enter your first Number:- ")),)
        num2 = (int(input("Enter your Second Number:- ")),)
    except ValueError:
        print("Please enter a integer value!")
        return None
    choice = input(
        "Which operation you want to perform (Sum,difference,Multiply,Divide,Exponent and Square):- "
    ).lower()
    if (
        choice == "sum"
        or choice == "multiply"
        or choice == "divide"
        or choice == "exponent"
        or choice == "square"
    ):
        if choice == "sum":
            print(num1 + num2)
        elif choice == "difference":
            print(num1 - num2)
        elif choice == "divide":
            print(num1 // num2)
        elif choice == "multiply":
            print(num1 * num2)
        elif choice == "exponent":
            print(num1**num2)
        else:
            print(num1**2, num2**2)
    else:
        print("Please select a valid input")


calculator()
