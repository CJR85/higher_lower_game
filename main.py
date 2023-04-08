from art import logo, vs
from game_data import data
import random

# Format data into printable data
def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return (f"{account_name} a {account_descr} from {account_country}")

# Display ASCII art
print(logo)

# Generate game data
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_a = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Against B: {format_data(account_b)}.")

# Ask user to enter a guess

# Check if user's guess is correct
# Get follower count of each account
# Use if statement to check if user is correct

# User feedback on their answer

# Score keeping

# Make game repeatable

# Making account at position B become account at position A

# Clear screen between rounds