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
            choice=input("Do you want to update,delete or show the contacts or search contact(update,delete,show,search):- ").lower()
            if choice=='update':
                name = input("Enter the person name:- ").capitalize()
                number = input(
                    "Enter the user number (please write in this format(+countrycode number)):- "
                    )
                if name in contact.keys():
                    contact[name]=number
                else:
                    newContact=input(f"there is no {name} do you want to create this contact(yes/no)").lower()
                    if newContact=='yes':
                        contact[name]=number
                        print('Added Successfully')
                    else:
                        break
                        
            if choice=='delete':
                name = input("Enter the person name:- ").capitalize()
                if name in contact.keys():
                    del contact[name]
                    print("deleted successFully")
                else:
                    print("this contact is not on your app")
                
            if choice=='search':
                name = input("Enter the person name:- ").capitalize()
                if name in contact.keys():
                    print(contact[name])
                else:
                    print('this is not in your contact list')
            else:
                for person, number in contact.items():
                    print(f"{person}:{number}")
        newChoice = input("Do you want to exit the app (Yes/No)").lower()
        if newChoice != "no":
            break

contactBook()