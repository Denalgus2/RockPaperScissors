import random


def rock_paper_scissors(winner):
    winner = 0
    user_input = input("Rock, Paper, or Scissors? ").lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    if input == computer:
        print("It's a tie!")
    elif user_input == "rock" and computer == "scissors" or user_input == "paper" and computer == "rock" or user_input == "scissors" and computer == "paper":
        print("Computer chose " + computer)
        print("You win!")
        return winner + 1
    else:
        print("Computer chose " + computer)
        print("You lose!")
        return winner


rounds = int(input("How many rounds do you want to play? "))
y_points = 0
c_points = 0
win = 0
for i in range(rounds):
    rock_paper_scissors(win)
    if win == 1:
        y_points += 1
    else:
        c_points += 1
    print("You: " + str(y_points), "AI: " + str(c_points))

