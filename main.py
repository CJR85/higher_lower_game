from art import logo, vs
from game_data import data
import random

# Format data into printable data
def format_data(account):
  """Takes account data and returns printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return (f"{account_name} a {account_descr} from {account_country}")

# Use if statement to check if user is correct
def check_answer(guess, a_followers, b_followers):
   """Takes users guess & follower counts & returns answer"""
   if a_followers > b_followers:
      return guess == "a"
   else:
      return guess == "b"

# Display ASCII art
print(logo)
score = 0
continue_game = True
# Generate game data
account_b = random.choice(data)

# Make game repeatable
while continue_game:

  # Making account at position B become account at position A
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
   account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  # Ask user to enter a guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check if user's guess is correct
  # Get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear screen between rounds
  print("\033[2J\033[1;1H")

  # User feedback on their answer
  # Score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    continue_game = False
    print(f"Sorry, you're wrong. Final score: {score}")




