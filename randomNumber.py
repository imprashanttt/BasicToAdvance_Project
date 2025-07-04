import random

rand_num=random.randint(1,10)

while True:
    user=int(input("Guess your number:- "))
    if user==rand_num:
        print("You guessed right number")
        break
    elif user>rand_num:
        print("Your guessed number is greater the actual number")
    else:
        print("Your guessed number is slightly smaller than guessed number")

