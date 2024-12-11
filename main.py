from art import logo
import random

# Sets constants for turn count
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 7

turns = 0
answer = random.randint(1,100)

# Function to compare guess to the targdet
def check_guess(user_guess, actual_answer, turns):
	"""Checks guess against answer and returns the turns remaining"""
	if user_guess > actual_answer:
		print("Too high!")
		return turns - 1
	elif user_guess < actual_answer:
		print("Too low!")
		return turns - 1
	else:
		print(f"You got it! The answer is {actual_answer}.")

# Function to set difficulty
def set_difficulty():
	level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
	if level == "easy":
		return EASY_LEVEL_TURNS
	elif level == "hard":
		return HARD_LEVEL_TURNS
	else:
		# Rerun the function until valid entry
		set_difficulty()

print(logo)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# call function and return number of turns
turns = set_difficulty()

# Show answer for testing
# print(f"Here's the answer: {answer}")

# Initialize guess count as integer
guess = 0

# Run this while guess does not match target number until guess count is zero
while guess != answer:
	if turns == 0:
		print("You're out of guesses.  You lose.")
		print(f"The target number was: {answer}")
		guess = answer  # creative way to end the while loop
	else:
		print(f"You have {turns} guesses remaining.")
		guess = int(input("Make a guess: "))
		turns = check_guess(guess, answer, turns)
		