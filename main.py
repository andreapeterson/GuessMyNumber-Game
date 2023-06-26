import os
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo
import random

print("Welcome to Guess the Number! Can you guess what number I am thinking of?")

answer=random.randint(1,100)


attempts=0
def game_route():
  global attempts
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty== "easy":
    attempts=10
  else:
    attempts=5
  should_continue=True
  while should_continue:
    print(f"You have {attempts} attempts remaining to guess the number")
    guess=int(input("Make a guess: "))
    if guess < answer:
      print("Too low")
      attempts-= 1
      if attempts>0:
        print("Guess again.")
      else:
        should_continue=False
        print(f"I win! You have no guesses left. My number was {answer}.")
    elif guess > answer:
      print("Too high.")
      attempts-= 1
      if attempts>0:
        print("Guess again.")
      else:
        should_continue=False
        print(f"I win! You have no guesses left. My number was {answer}.")
    else:
      print("You win! That was my number.")
      should_continue=False

    
def play_game():
  print(logo)
  print("Hmmm, I am thinking of a number 1 through 100.")
  game_route()
 

while input("If you want to play type 'y', else type 'n': ") == "y":
  clear()
  play_game()
else:
  clear()
  print("Thank you for playing! Come back soon!")