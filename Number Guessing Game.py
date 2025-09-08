#Number Guessing Game
import random
tries = 0
print("Welcome to the Number Guessing Game!\nHow to play:\nGuess a random number between 1 to 100.\n")
answer = random.randint(1, 100)
while True:
    choice = int(input("Enter your choice: "))
    tries += 1
    if choice == answer:
        print(f"Congratulations!You guessed correct.\nYou finished the game in {tries} chances")
        break
    elif choice < answer:
        print("Too low!")
    elif choice > answer:
        print("Too high!")
    else:
        print("Invalid Choice")
        