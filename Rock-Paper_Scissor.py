#Rock-Paper_Scissor
import random
game_objects = {
    "rock" : "🪨",
    "paper" : "📄",
    "scissor" : "✂️"}

computer_score = 0
user_score = 0
name = input("Welcome to my game: \nWhat should we call you?")

while True:
    computer_choice = random.choice(list(game_objects.keys()))
    user_choice = input("Enter your choice(Rock 🪨, Paper 📄, Scissor ✂️)").strip().lower()

    if user_choice not in game_objects:
        print("Invalid")
        continue

    print(f"Computer chose {computer_choice}{game_objects[computer_choice]}")
    
    if computer_choice == user_choice:
        print(f"It's a tie!")
    elif computer_choice == "scissor" and user_choice =="rock" or computer_choice == "rock" and user_choice == "paper" or computer_choice == "paper" and user_choice == "scissor":
        user_score += 1
        print(f"{name} won!")
    else:
        computer_score += 1
        print("Computer won!") 

    print(f"Computer: {computer_score} and {name}: {user_score} ")
    
    question = input("Do you want to play again?").strip().lower()
    
    if question not in ("yes", "y"):
        break
    else:
        continue
    