import random
def tutorial_mode():
    briefcase_values = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
    random.shuffle(briefcase_values)

    return briefcase_values


def banker_offer(remaining_briefcases):
    briefcase=tutorial_mode()
    total_value = sum(briefcase)
    remaining = len(remaining_briefcases)
    return total_value / remaining

def deal_or_no_deal():
    # Display the available briefcases
    print("There are 26 briefcases which all contain a different cash prize ranging from $0.01 to $1,000,000 \n")
   
       
    print("Welcome to Deal or No Deal Tutorial \n")
    print("Game Begins\n")
    briefcases=tutorial_mode()    

    remaining_cases = list(range(1, 27))
    print("Available briefcases are \n")
    print(*remaining_cases,sep="," )    
    print()
    remaining_briefcases = briefcases[:]
   
   
    print("In tutorial mode we have 4 rounds, however in actual mode we can go upto 10 rounds\n")
    print("Game begins with user selecting a briefcase to open. Once the briefcase is open, the value is removed from banker offer\n")
    print("Goal of the game is for user to pick as many low value briefcases so that the banker offer is high\n")
   
    num_rounds = 4
    for i in range(num_rounds):
        # Open a briefcase at random and reveal its value
        briefcase_to_open = int(input("Choose a briefcase to open (1-26): "))
        briefcase_to_open_value = remaining_briefcases[briefcase_to_open-1]
       
        remaining_briefcases.remove(briefcase_to_open_value)
       
        print(f"You have opened briefcase {briefcase_to_open} with a value of ${briefcase_to_open_value}")
        print()
        remaining_cases.remove(briefcase_to_open)
        print("Available Cases are:\n")
        print(*remaining_cases,sep=",")
       
        print(f"You have following values remaining in briefcases\n")
        remaining_values=sorted(remaining_briefcases)        
        print(*remaining_values,sep=",")
       
               
       
        # Calculate the expected value of the remaining briefcases
        remaining_value = banker_offer(remaining_briefcases)
        print(f"Bank offers you this is ${remaining_value:.2f}\n")

        # Ask the user if they want to deal or not

        # Ask the user if they want to deal or not
        deal = input("Enter 'D' to deal or 'N' for no deal? ")
        if deal == "D":
            winning_amt=remaining_value
            print(f"You took a deal of ${remaining_value:.2f}")
            return winning_amt
           
           
           
    winning_amt=random.choice(remaining_briefcases)
    print(f"Congratulations! You won {winning_amt}")
    return winning_amt