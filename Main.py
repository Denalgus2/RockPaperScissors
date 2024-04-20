import random

def rock_paper_scissors():

    user_input=input("Rock, Paper, or Scissors? ").lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    if input == computer:
        print("It's a tie!")
    elif user_input == "rock" and computer == "scissors":
        print("You win!")

