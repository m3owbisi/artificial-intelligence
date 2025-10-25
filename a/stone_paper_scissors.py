import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors: ")
computer = random.choice(choices)

print(f"\nYou chose: {user}")
print(f"Computer chose: {computer}")

if user not in choices:
    print("Invalid choice!")
elif user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")
