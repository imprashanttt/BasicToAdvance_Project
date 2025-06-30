"""this contact book app where we manage the contact of the user he can check contact book
add new contact , update , delete and also search specific contact
just using dictionary ,function and loops
"""

contact = {}


def contactBook():
    print("Welcome to the contact book app")
    while True:
        choice = input("Do you want to create a contact (Yes/No)").lower()
        if choice == "yes":
            name = input("Enter the person name:- ").capitalize()
            number = input(
                "Enter the user number (please write in this format(+countrycode number)):- "
            )
            contact[name] = number
        else:
            for person, number in contact.items():
                print(f"{person}:{number}")
        newChoice = input("Do you want to exit the app (Yes/No)").lower()
        if newChoice != "no":
            break

contactBook()