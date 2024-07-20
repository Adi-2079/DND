import audioop
from simple_colors import *
import random
import time
import os
import multi
import login

def login():
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password are valid
    with open("users.txt", "r") as f:
        for line in f:
            line = line.strip()  # Remove leading/trailing whitespaces
            if not line:
                continue  # Skip empty lines

            try:
                user, passw = line.split()
                if username == user and password == passw:
                    print("Login successful!")
                    return True
            except ValueError:
                print("Invalid user data format in the file.")
                return False

    # Display an error message
    print("Invalid username or password")
    return False


def register():
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username already exists
    with open("users.txt", "r") as f:
        for line in f:
            line = line.strip()  # Remove leading/trailing whitespaces
            if not line:
                continue  # Skip empty lines

            try:
                user, passw = line.split()
                if username == user:
                    print("Username already taken")
                    return False
            except ValueError:
                print("Invalid user data format in the file.")
                return False

    # Write the username and password to the text file
    with open("users.txt", "a") as f:
        f.write(f"{username} {password}\n")

    print("Registration successful!")
    return True


def main():
    while True:
        print("Welcome to the login system!")
        print("Choose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            if login():
                # Perform logged-in operations
                print("Logged in. Access granted.")
                break  # Exit the loop after successful login
        elif choice == "2":
            if register():
                # Perform post-registration operations
                print("Registration complete. You can now login.")
        elif choice == "3":
            break  # Exit the loop if the user chooses to quit
        else:
            print("Invalid choice. Please try again.")


# Call the main function to start the login system
main()
def deal_or_no_deal_briefcases():
   global briefcases
   global remaining_briefcases
   briefcases = {}
   amount = [0.1, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
   for i in range (1,27):
       briefcases[str(i)] = amount.pop(amount.index(random.choice(amount)))
       remaining_briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
   return briefcases, remaining_briefcases
  
def list_to_string(lst):
   return ' '.join(map(str, lst))

def deal_or_no_deal():
     pass





def player_briefcase(remaining_briefcases):
   global chosen_briefcase
   print("You must pick a briefcase from 1-26 and this briefcases will be kept safe throughout the game. Remember the number of your briefcase as you will need it later. ")
   chosen_briefcase = int(input("Chosen briefcase: "))
   while chosen_briefcase not in range(1, 27):
       print("Sorry. This number is not valid. Please pick again")
       chosen_briefcase = int(input("Chosen briefcase: "))
   remaining_briefcases.remove(chosen_briefcase)
   print("You chose briefcase " + str(chosen_briefcase))
   return chosen_briefcase, remaining_briefcases





def get_random_offer():
   return round(random.uniform(10, 120000), 2)