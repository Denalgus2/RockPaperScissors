import random


def rock_paper_scissors(y_points, c_points):
    user_input = input("Rock, Paper, or Scissors? ").lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    if input == computer:
        print("It's a tie!")
    elif user_input == "rock" and computer == "scissors" or user_input == "paper" and computer == "rock" or user_input == "scissors" and computer == "paper":
        print("Computer chose " + computer)
        print("You win!")
        y_points += 1
    else:
        print("Computer chose " + computer)
        print("You lose!")
        c_points += 1


rounds = int(input("How many rounds do you want to play? "))

for i in range(rounds):
    rock_paper_scissors(y_points=0, c_points=0)

