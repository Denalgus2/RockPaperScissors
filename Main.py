import random
import os

def rock_paper_scissors(winner):
    winner = 0
    user_input = input("Rock, Paper, or Scissors? ").lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    if user_input == computer:
        print("It's a tie!")
    elif user_input == "rock" and computer == "scissors" or user_input == "paper" and computer == "rock" or user_input == "scissors" and computer == "paper":
        print("Computer chose " + computer)
        print("You win!")
        return winner + 1
    else:
        print("Computer chose " + computer)
        print("You lose!")
        return winner + 2


rounds = int(input("How many rounds do you want to play? "))
y_points = 0
c_points = 0
win = 0
for i in range(rounds):
    print("Round", i+1, "of", rounds)
    win = rock_paper_scissors(win)

    if win == 1:
        y_points += 1
    elif win == 2:
        c_points += 1

    print("You: " + str(y_points), "AI: " + str(c_points))
    cont=str(input("Press enter to continue: "))
    print("\n"*10)

print("\n"*100)
if y_points > c_points:
    print("Congrats, you won against the AI!")
elif c_points > y_points:
    print("You lost against the AI!")

