import random
# Set up the initial game variables
briefcases = list(range(1, 27))
prize_amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
chosen_cases = []
players = []

# Define the functions for the game
def print_board():
    print("Here are the remaining briefcases:")
    for briefcase in briefcases:
        if briefcase not in chosen_cases:
            print(briefcase, end=' ')
    print("\n")

def offer():
    total_prize_amount = sum(prize_amounts)
    average_prize_amount = total_prize_amount / len(briefcases)
    offer_amount = round(average_prize_amount * 0.5, 2)
    return offer_amount
    
def play_game():
    print("""
                                                                  
@@@@@@@   @@@@@@@@   @@@@@@   @@@           @@@@@@   @@@@@@@   
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@          @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!       @@!  @@@  @@!          @@!  @@@  @@!  @@@  
!@!  @!@  !@!       !@!  @!@  !@!          !@!  @!@  !@!  @!@  
@!@  !@!  @!!!:!    @!@!@!@!  @!!          @!@  !@!  @!@!!@!   
!@!  !!!  !!!!!:    !!!@!!!!  !!!          !@!  !!!  !!@!@!    
!!:  !!!  !!:       !!:  !!!  !!:          !!:  !!!  !!: :!!   
:!:  !:!  :!:       :!:  !:!   :!:         :!:  !:!  :!:  !:!  
 :::: ::   :: ::::  ::   :::   :: ::::     ::::: ::  ::   :::  
:: :  :   : :: ::    :   : :  : :: : :      : :  :    :   : :  
                                                               
                                                               
@@@  @@@   @@@@@@      @@@@@@@   @@@@@@@@   @@@@@@   @@@       
@@@@ @@@  @@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@       
@@!@!@@@  @@!  @@@     @@!  @@@  @@!       @@!  @@@  @@!       
!@!!@!@!  !@!  @!@     !@!  @!@  !@!       !@!  @!@  !@!       
@!@ !!@!  @!@  !@!     @!@  !@!  @!!!:!    @!@!@!@!  @!!       
!@!  !!!  !@!  !!!     !@!  !!!  !!!!!:    !!!@!!!!  !!!       
!!:  !!!  !!:  !!!     !!:  !!!  !!:       !!:  !!!  !!:       
:!:  !:!  :!:  !:!     :!:  !:!  :!:       :!:  !:!   :!:      
 ::   ::  ::::: ::      :::: ::   :: ::::  ::   :::   :: ::::  
::    :    : :  :      :: :  :   : :: ::    :   : :  : :: : :  
                                                               
                                                                             
@@@@@@@@@@   @@@  @@@  @@@       @@@@@@@  @@@  @@@@@@@   @@@        @@@@@@   
@@@@@@@@@@@  @@@  @@@  @@@       @@@@@@@  @@@  @@@@@@@@  @@@       @@@@@@@@  
@@! @@! @@!  @@!  @@@  @@!         @@!    @@!  @@!  @@@  @@!       @@!  @@@  
!@! !@! !@!  !@!  @!@  !@!         !@!    !@!  !@!  @!@  !@!       !@!  @!@  
@!! !!@ @!@  @!@  !@!  @!!         @!!    !!@  @!@@!@!   @!!       @!@!@!@!  
!@!   ! !@!  !@!  !!!  !!!         !!!    !!!  !!@!!!    !!!       !!!@!!!!  
!!:     !!:  !!:  !!!  !!:         !!:    !!:  !!:       !!:       !!:  !!!  
:!:     :!:  :!:  !:!   :!:        :!:    :!:  :!:        :!:      :!:  !:!  
:::     ::   ::::: ::   :: ::::     ::     ::   ::        :: ::::  ::   :::  
 :      :     : :  :   : :: : :     :     :     :        : :: : :   :   : :  
                                                                             
                                                                           
@@@ @@@  @@@@@@@@  @@@@@@@      @@@@@@@@@@    @@@@@@   @@@@@@@   @@@@@@@@  
@@@ @@@  @@@@@@@@  @@@@@@@@     @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
@@! !@@  @@!       @@!  @@@     @@! @@! @@!  @@!  @@@  @@!  @@@  @@!       
!@! @!!  !@!       !@!  @!@     !@! !@! !@!  !@!  @!@  !@!  @!@  !@!       
 !@!@!   @!!!:!    @!@!!@!      @!! !!@ @!@  @!@  !@!  @!@  !@!  @!!!:!    
  @!!!   !!!!!:    !!@!@!       !@!   ! !@!  !@!  !!!  !@!  !!!  !!!!!:    
  !!:    !!:       !!: :!!      !!:     !!:  !!:  !!!  !!:  !!!  !!:       
  :!:    :!:       :!:  !:!     :!:     :!:  :!:  !:!  :!:  !:!  :!:       
   ::     :: ::::  ::   :::     :::     ::   ::::: ::   :::: ::   :: ::::  
   :     : :: ::    :   : :      :      :     : :  :   :: :  :   : :: ::   
                                                                                                     """)
    # Ask for the number of players
    num_players = int(input("How many players? "))
    
    # Get the player names
    for i in range(num_players):
        player_name = input(f"What is player {i+1}'s name? ")
        players.append(player_name)
    
    # Randomly choose a briefcase for each player
    for player_name in players:
        chosen_case = random.choice(briefcases)
        chosen_cases.append(chosen_case)
        briefcases.remove(chosen_case)
        print(f"{player_name}, your chosen briefcase is: {chosen_case}")
    
    # Play the rounds
    num_rounds = 6
    for round_num in range(num_rounds):
        print(f"\n\nRound {round_num+1}")
        print_board()
        for player_num, player_name in enumerate(players):
            if player_name not in chosen_cases:  # Only play if player is still in the game
                print(f"\n{player_name}, it's your turn!")
                chosen_briefcase = int(input("Which briefcase do you choose? "))
                briefcases.remove(chosen_briefcase)
                prize_amount = prize_amounts.pop(random.randrange(len(prize_amounts)))
                print(f"You have eliminated ${prize_amount}!")
                if chosen_briefcase == chosen_cases[player_num]:
                    print(f"\n{player_name}, you have won ${prize_amount} and your original briefcase is worth ${chosen_briefcase}!")
                    chosen_cases.remove(chosen_briefcase)
    
    # Final round
    print("\n\nFinal Round!")
    offer_amount = offer()
    for player_num, player_name in enumerate(players):
        if player_name not in chosen_cases:  # Only play if player is still in the game
            print(f"\n{player_name}, it's your turn!")
            print_board()
            deal_or_no_deal = input(f"You have been offered ${offer_amount}. Deal or no deal? ")
            if deal_or_no_deal.lower() == "deal":
                print(f"\nCongratulations, {player_name}! You have won ${offer_amount}!")
            else:
                print(f"\n{player_name}, you chose not to take the deal. Let's see what's in your briefcase...")
                prize_amount = chosen_cases[player_num]
                print(f"Your original briefcase was worth ${prize_amount}.")
    
    # Determine the final results
    remaining_players = [player for player in players if player in chosen_cases]
    if len(remaining_players) == 0:
        print("\n\nAll players have won!")
    else:
        print("\n\nBetter luck next time for the following players:")
        for player_name in remaining_players:
            print(player_name)


# Start the game