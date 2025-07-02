import re

""" Project 4: User Registration System (Concepts: Input Validation, String Methods)
Purpose: Create a system where users can register with email and password.

Key concepts: String methods, input validation, and basic file handling (to save data)."""


emailRegex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def registerUser():
    email = input("Enter your Email:- ").strip()
    password = input("Enter your Password:_ ").strip()
    pass_length = len(password)
    if emailRegex.fullmatch(email) and pass_length >= 8:
        with open("./userData.txt", "a") as userFile:
            userFile.write(f"email:-{email} password:-{password} \n")
            print("You are successfully registered")
    else:
        print(
            "Please check your email and password Note Password must have 8 character"
        )


registerUser()
