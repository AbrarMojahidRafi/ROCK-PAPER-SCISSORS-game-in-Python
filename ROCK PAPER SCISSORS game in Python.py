import random

options = ("rock", "paper", "scissors")
computer = random.choice(options)

you = input("Enter a choice (rock/paper/scissors): ")
if you not in options: 
    print('Please enter a valid choice.')

print(computer, you)