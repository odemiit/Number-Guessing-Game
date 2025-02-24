# A number guessing game where the user has to guess a number between 1 and 100

#Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

#Function to set the difficulty level
def set_difficulty():
  game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  #Set number of lives based on the difficulty chosen
  if game_difficulty == "easy":
    return EASY_LEVEL_LIVES
  elif game_difficulty == "hard":
    return HARD_LEVEL_LIVES
  else:
    print("You've chosen an invalid difficulty. Try again!")

#Print out logo and welcome messages
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Generate a random number between 1 and 100
answer = random.randint(1,100)
no_of_lives = set_difficulty()

#Loop through based on the number of lives left to figure out the correct number
while no_of_lives > 0:
  print(f"You have {no_of_lives} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))

  if guess > answer:
    print("Too high.")
    no_of_lives -= 1

    if no_of_lives == 0:
      print("You've run out of guesses, you lose!")
    else:
      print("Guess again.")
      
  elif guess < answer:
    print("Too low.")
    no_of_lives -= 1

    if no_of_lives == 0:
      print("You've run out of guesses, you lose!")
    else:
      print("Guess again.")
      
  elif guess == answer:
    print(f"You got it! The answer was {guess}")
    no_of_lives = 0
