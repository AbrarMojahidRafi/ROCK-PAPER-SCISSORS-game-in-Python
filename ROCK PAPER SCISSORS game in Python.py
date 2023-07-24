import random

options = ("rock", "paper", "scissors")
generateComputerChoice = random.choice(options)

yourChoice = input("Enter a choice (rock/paper/scissors): ").lower()
if yourChoice not in options:
    print('Please enter a valid choice.')
else: 
  print(f"COMPUTER CHOICE: {generateComputerChoice}")
  print(f"YOU CHOICE: {yourChoice}")
  print("="*22)
  if generateComputerChoice == yourChoice:
    print("Game TIE")
  else:
    if (generateComputerChoice == "rock" and yourChoice == "scissors") or (generateComputerChoice == "paper" and yourChoice == "rock") or (generateComputerChoice == "scissors" and yourChoice == "paper"):
      print("COMPUTER wins the game!")
    else:
      print("YOU wins the game!")

