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

def deal_or_no_deal(): #round one
  
   briefcases, remaining_briefcases = deal_or_no_deal_briefcases()
   player_briefcase_num, remaining_briefcases = player_briefcase(remaining_briefcases)
   number_of_briefcases_to_eliminate = 6
   while len(remaining_briefcases) >19:
           briefcases_left = list_to_string(remaining_briefcases)
          
           print("Chose the briefcases to eliminate from the following list")
           print(green(briefcases_left, ("bold")))
           briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
           if briefcase_to_eliminate not in remaining_briefcases:
               print("Sorry. Briefcase has already been chosen. Please pick again.")
               time.sleep(6)
               os.system("clear")
               continue
           remaining_briefcases.remove(briefcase_to_eliminate)
           if str(briefcase_to_eliminate) in briefcases:
                briefcase_content = briefcases[str(briefcase_to_eliminate)]
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(4)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
         offer = get_random_offer()
         print("The bank is thinking of an offer")
         time.sleep(1.5)
         print("The offer is.....")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("The bank's offer is: ", offer)
         print("Please type D to accept this deal and N to decline this deal and keep playing")
         time.sleep(4)
         os.system("clear")
        
         decision = input("Selection: ")
         if decision == "D":
                   print("You have won $ ", offer, "the game has ended!")
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer

         elif decision == "N":
                    print("You have declined $ ", offer, "let us continue to the next round.")
                    print("The first round has ended. In the second round you will pick 5 briefcases to be eliminated.")
                    time.sleep(8)
                    os.system("clear")
                    break
         if decision == "N":
           while len(remaining_briefcases) >14: #round 2
               briefcases_left = list_to_string(remaining_briefcases)
          
               print("Chose the briefcases to eliminate from the following list")
               print(green(briefcases_left, ("bold")))
               briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
               if briefcase_to_eliminate not in remaining_briefcases:
                   print("Sorry. Briefcase has already been chosen. Please pick again.")
               else:
                   remaining_briefcases.remove(briefcase_to_eliminate)
               if str(briefcase_to_eliminate) in briefcases:
                   briefcase_content = briefcases[str(briefcase_to_eliminate)]
                   print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                   time.sleep(4)
                   os.system("clear")
               else:
                   print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
          offer = get_random_offer()
          print("The bank is thinking of an offer")
          time.sleep(1.5)
          print("The offer is.....")
          time.sleep(1.5)
          print("...")
          time.sleep(1.5)
          print("...")
          time.sleep(1.5)
          print("The bank's offer is: ", offer)
          print("Please type D to accept this deal and N to decline this deal and keep playing")
          time.sleep(4)
          os.system("clear")
      
          decision = input("Selection: ")
          if decision == "D":
                   
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer

          
          elif decision== "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The second round has ended. You will pick 4 to be discarded from the list.")
                time.sleep(5.5)
                break
              
   if decision== "N":
       while len(remaining_briefcases) >10: #round 3
           briefcases_left = list_to_string(remaining_briefcases)
          
           print("Chose the briefcases to eliminate from the following list")
           print(green(briefcases_left, ("bold")))
           briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
           if briefcase_to_eliminate not in remaining_briefcases:
               print("Sorry. Briefcase has already been chosen. Please pick again.")
               time.sleep(4.5)
               os.system("clear")
               continue
           remaining_briefcases.remove(briefcase_to_eliminate)
           if str(briefcase_to_eliminate) in briefcases:
                briefcase_content = briefcases[str(briefcase_to_eliminate)]
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(3.5)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
         offer = get_random_offer()
         print("The bank is thinking of an offer")
         time.sleep(1.5)
         print("The offer is.....")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("The bank's offer is: ", offer)
         print("Please type D to accept this deal and N to decline this deal and keep playing")
         time.sleep(4)
         os.system("clear")
         
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The third round has ended. In the fourth round you will pick 3 briefcases to be eliminated ")
                time.sleep(5.5)
                break
   if decision == "N":
       while len(remaining_briefcases) >7: #round 4
           briefcases_left = list_to_string(remaining_briefcases)
          
           print("Chose the briefcases to eliminate from the following list")
           print(green(briefcases_left, ("bold")))
           briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
           if briefcase_to_eliminate not in remaining_briefcases:
               print("Sorry. Briefcase has already been chosen. Please pick again.")
               time.sleep(4.5)
               os.system("clear")
               continue
           remaining_briefcases.remove(briefcase_to_eliminate)
           if str(briefcase_to_eliminate) in briefcases:
                briefcase_content = briefcases[str(briefcase_to_eliminate)]
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(3.5)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
         offer = get_random_offer()
         print("The bank is thinking of an offer")
         time.sleep(1.5)
         print("The offer is.....")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("The bank's offer is: ", offer)
         print("Please type D to accept this deal and N to decline this deal and keep playing")
         time.sleep(4)
         os.system("clear")
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The fourth round has ended. You will now pick 2 briefcase to be discarded from the list.")
                time.sleep(5.5)
                break
   if decision == "N":
       while len(remaining_briefcases) >5:#round 5
           briefcases_left = list_to_string(remaining_briefcases)
          
           print("Chose the briefcases to eliminate from the following list")
           print(green(briefcases_left, ("bold")))
           briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
           if briefcase_to_eliminate not in remaining_briefcases:
               print("Sorry. Briefcase has already been chosen. Please pick again.")
               time.sleep(3.5)
               os.system("clear")
               continue
           remaining_briefcases.remove(briefcase_to_eliminate)
           if str(briefcase_to_eliminate) in briefcases:
                briefcase_content = briefcases[str(briefcase_to_eliminate)]
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(4)
                os.system("clear")
           else:
                print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
         offer = get_random_offer()
         print("The bank is thinking of an offer")
         time.sleep(1.5)
         print("The offer is.....")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("The bank's offer is: ", offer)
         print("Please type D to accept this deal and N to decline this deal and keep playing")
         time.sleep(4)
         os.system("clear")
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The fifth round has ended. You will now pick 1 briefcase to be discarded from the list.")
                time.sleep(5.5)
                break
   if decision == "N":
       while len(remaining_briefcases) >4: #round 6
           briefcases_left = list_to_string(remaining_briefcases)
          
           print("Chose the briefcases to eliminate from the following list")
           print(green(briefcases_left, ("bold")))
           briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
           if briefcase_to_eliminate not in remaining_briefcases:
               print("Sorry. Briefcase has already been chosen. Please pick again.")
               time.sleep(6)
               os.system("clear")
               continue
           remaining_briefcases.remove(briefcase_to_eliminate)
           if str(briefcase_to_eliminate) in briefcases:
                briefcase_content = briefcases[str(briefcase_to_eliminate)]
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(6)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
         offer = get_random_offer()
         print("The bank is thinking of an offer")
         time.sleep(1.5)
         print("The offer is.....")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("The bank's offer is: ", offer)
         print("Please type D to accept this deal and N to decline this deal and keep playing")
         time.sleep(4)
         os.system("clear")
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The sixth round has ended. You will now pick 1 briefcase to be discarded from the list.")
                time.sleep(5.5)
                break
   if decision == "N":
       while len(remaining_briefcases) >3: #round 7
           briefcases_left = list_to_string(remaining_briefcases)
          
           print("Chose the briefcases to eliminate from the following list")
           print(green(briefcases_left, ("bold")))
           briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
           if briefcase_to_eliminate not in remaining_briefcases:
               print("Sorry. Briefcase has already been chosen. Please pick again.")
               time.sleep(6)
               os.system("clear")
               continue
           remaining_briefcases.remove(briefcase_to_eliminate)
           if str(briefcase_to_eliminate) in briefcases:
                briefcase_content = briefcases[str(briefcase_to_eliminate)]
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(4)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
         offer = get_random_offer()
         print("The bank is thinking of an offer")
         time.sleep(1.5)
         print("The offer is.....")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("The bank's offer is: ", offer)
         print("Please type D to accept this deal and N to decline this deal and keep playing")
         time.sleep(4)
         os.system("clear")
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The seventh round has ended. In the eigth round, you will pick one briefcase to be eliminated.")
                time.sleep(5.5)
                break
   if decision == "N":
       while len(remaining_briefcases) >2: #round 8
           briefcases_left = list_to_string(remaining_briefcases)
          
           print("Chose the briefcases to eliminate from the following list")
           print(green(briefcases_left, ("bold")))
           briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
           if briefcase_to_eliminate not in remaining_briefcases:
               print("Sorry. Briefcase has already been chosen. Please pick again.")
               time.sleep(6)
               os.system("clear")
               continue
           remaining_briefcases.remove(briefcase_to_eliminate)
           if str(briefcase_to_eliminate) in briefcases:
                briefcase_content = briefcases[str(briefcase_to_eliminate)]
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(4)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
       while True:
         offer = get_random_offer()
         print("The bank is thinking of an offer")
         time.sleep(1.5)
         print("The offer is.....")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("The bank's offer is: ", offer)
         print("Please type D to accept this deal and N to decline this deal and keep playing")
         time.sleep(4)
         os.system("clear")

         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The eigth round has ended. In the ninth round you will pick one briefcase to be eliminated")
                time.sleep(5.5)
                break
   
   if decision =="N":
       while len(remaining_briefcases) >1: #round 9
           briefcases_left = list_to_string(remaining_briefcases)
          
           print("Chose the briefcases to eliminate from the following list")
           print(green(briefcases_left, ("bold")))
           briefcase_to_eliminate = int(input("Eliminated briefcase:\n "))
           if briefcase_to_eliminate not in remaining_briefcases:
               print("Sorry. Briefcase has already been chosen. Please pick again.")
               time.sleep(4.5)
               os.system("clear")
               continue
           remaining_briefcases.remove(briefcase_to_eliminate)
           if str(briefcase_to_eliminate) in briefcases:
                briefcase_content = briefcases[str(briefcase_to_eliminate)]
                print("You removed briefcase", briefcase_to_eliminate, "which contained $ ", briefcase_content)
                time.sleep(6)
                os.system("clear")
           else:
               print("Briefcase ", briefcase_to_eliminate, "has already been removed.")
   while True:
         offer = get_random_offer()
         print("The bank is thinking of an offer")
         time.sleep(1.5)
         print("The offer is.....")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("...")
         time.sleep(1.5)
         print("The bank's offer is: ", offer)
         print("Please type D to accept this deal and N to decline this deal and keep playing")
         time.sleep(4)
         os.system("clear")
      
         decision = input("Selection: ")
         if decision == "D":
                   os.system("clear")
                   print("You have won $ ", offer, "the game has ended!")
                   return get_random_offer
         elif decision== "N":
                print("You have declined $ ", offer, "let us continue to the next round.")
                print("The ninth round has ended. You will now pick between your original briefcase and the final briefcase.")
                time.sleep(5.5)
                break
   if decision == "N":
    if len(remaining_briefcases) >0: # round 10
           remaining_briefcases.append(chosen_briefcase)
           briefcases_left = list_to_string(remaining_briefcases)
          
           print(" Your original briefcase has been added to the list. You must pick between your original briefcase and the other briefcase left in the list.")
           print(green(briefcases_left, ("bold")))
           print("Type the number of the original briefcase to choose the original briefcase, or the number in the list to choose the remaining briefcase.")

           briefcase_won = int(input("Briefcase won:\n "))
           if briefcase_won == chosen_briefcase:
               remaining_briefcases.remove(briefcase_won)
               print("You have won...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               briefcase_content = briefcases[str(briefcase_won)]
               print("You just won...... $ ", briefcase_content)
               time.sleep(10)
               os.system("clear")
           elif briefcase_won in remaining_briefcases:
               remaining_briefcases.remove(briefcase_won)


               print("You have won...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               print("...")
               time.sleep(1.5)
               briefcase_content = briefcases[str(briefcase_won)]
               print("You just won...... $ ", briefcase_content)
               time.sleep(10)
               os.system("clear")
           else:
                  print("Sorry you have chosen the wrong briefcase please pick again.")
                  briefcase_won = int(input("Briefcase won:" ))
          

def instructions(briefcases):
    print("This is the game deal or no deal. Every one of the 26 briefcases has a random value from 1 cent to 1 million dollars! To begin, you will pick one briefcase which will be kept safe throughout the game.")
    print("There will be multiple rounds of this game. After every round, the bank will offer you a deal")
    print("If you accept that deal, you win the money. If not, you keep playing and eventually either accept an offer or win the money in either the first briefcase you chose or the last briefcase left.")
    print("Throughout the game, if you feel you have eliminated too many briefcases with high values, just accept the offer and walk away with bundles of cash!")
    print("Let's play!")
    print("Do you want to play multiplayer M or single player S?")
    choice = input("Chosen mode: ")
    if choice == "M":
        # Pass an empty list for chosen_cases since it is not used in multiplayer mode
        multi.board(briefcases, [])
        # Pass the prize_amounts list as an argument to the offer() function
        multi.offer(prize_amounts)
        multi.play_game()
    else:
        deal_or_no_deal()

    time.sleep(15)
    os.system("clear")

briefcases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
prize_amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]  # Define the prize_amounts list here
instructions(briefcases)


instructions(briefcases)