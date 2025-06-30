"""
In this ToDo project we gonna create list of todo
where we gonna provide user a method to remove, upload, delete and update todo
make priority on top 1 todo
just using list, function and loops
"""

import pprint

TODO_LIST = []
pprint.pp(TODO_LIST)


def Todo():
    print("Welcome to the Todo App")

    def show():
        for todo in TODO_LIST:
            print(todo)

    try:
        choice = input(
            "Would You want to create a new today or see your todo's (new/show):- "
        ).lower()
    except ValueError:
        print("Please enter a valid string! ")
    if choice == "new":
        while True:
            todo = input("Enter your todo:- ")
            priority: bool = input(
                "Did you make it on your top priority (True/False):- "
            ).lower()
            if priority=='true':
                TODO_LIST.insert(0, todo)
            else:
                TODO_LIST.append(todo)
            more = input("Do you want to create more Todos(Yes/No):-").lower()
            if more != "yes":
                print("Here is your Todos")
                show()

                break
    elif choice == "show":
        show()

    else:
        print("Please enter Valid Input")


Todo()


"""Future changes or updates:-
    user can changes the priority like enter todo and where you want to place in which number or top 10
    save todo to file 
    better exception handling and more 
    if needed user interface or this is created using class


"""