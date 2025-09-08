#Dice rolling game
import random

while True:
    choice = input("Do you want to roll(Yes/No)?").lower()
    
    if choice == "yes":
        print(random.randint(1,6))
    elif choice == "no":
        print("Thanks for playing")
        break
    else:
        print("Invalid Choice")
