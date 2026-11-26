# Players Dummy Data 
players = {
    "Umesh Sharma": 520,
    "Maya Lin": 585,
    "Liam O'Connor": 640,
    "Sofia Rossi": 710,
    "Noah Patel": 765,
    "Chloe Dubois": 820,
    "Mateo Silva": 875,
    "Hannah Kim": 930,
    "Lucas Meyer": 985,
    "Zara Ali": 1040,
    "Ethan Brooks": 1115,
    "Amara Okafor": 1190,
    "Oliver Novak": 1265,
    "Priya Nair": 1340,
    "Jacob Cohen": 1425,
    "Elena Popova": 1510,
    "Daniel Sato": 1620,
    "Isabella Cruz": 1745,
    "Vikram Rao": 1875,
    "Claire Vance": 1980,    
}

def challenge():
    print("\n" + "-"*40)
    print("WELCOME TO CHALLENGE MODE:")
    print("-"*40)
    print("NOTE: You can Challenge only the player \nwhose rating is more than yours.")

    # Check if both the players are available in the player dictionary
    while True:

        # take the player and challenger name by the player who is challenging
        challenger = input("\nEnter you name (Challenger): ")
        defender = input("Enter the player name you want to challenge (Defender): ")
        
        # Checks if the players are there in Dummy players dictionary
        if challenger in players and defender in players:

            # Prevent self-challenge
            if challenger == defender:
                print("ERROR: You cannot challenge yourself.")
                continue

            # Check is the the challenger rating is less than defender rating
            if players[defender] > players[challenger]:
                print("\nCHALLENGE ACCEPTER.")
                
                # Display Both Challenger's and Defender's Rating before the Challenge Game
                print(f"\nChallenger Rating Before challenge game: {players[challenger]}")
                print(f"Defender Rating Before challenge game: {players[defender]}")
                
                while True:
                    # Main challenge logic which determines the players ratings
                    game_result = input("\nPlease Enter the Game Result: ").strip().lower()
                  
                    if game_result in ["Win", "w"]:
                        print("\nThe Challenger has won the game.")
                        players[challenger] += 10
                        players[defender] -= 10
    
    
                    elif game_result in ["Loss", "l"]:
                        print("\nThe Defender has won the game.")
                        players[challenger] -= 10
                        players[defender] += 10
                    
    
                    elif game_result in ["Draw", "d"]:
                        print("\nGame has resulted in a draw. No changes in player ratings.")
                    
                    
                    else:
                        print("ERROR: Invalid Game Result.")
                        continue

                    # Display Both Challenger's and Defender's Rating after the Challenge Game
                    print(f"\nChallenger Rating After challenge game: {players[challenger]}")
                    print(f"Defender Rating After challenge game: {players[defender]}")
                    break

                break  
    
            else:
                print("\nCHALLENGE DENIED.")
                print("Please challenge a player whose rating is greater than yours.")
                continue
                
              
        else:
            print(f"\nPlayer '{challenger}' or '{defender}' doesn't exits, please try again")
            continue            
  

# Leader Board Display 
def leaderBoard(players):
    if not players:
        print("No Players to display")
        return
    
    print("\n" + "-"*45)
    print(f"{' ' * 2}Current Leader Board")
    print("-"*45)
    print(f"{' ' * 2}{'Rank':<8} | {'Player Name':<20} | {'Rating':<10}")
    print("-"*45)
    
    sorted_players = sorted(
        players.items(), 
        key=lambda x: x[1], 
        reverse=True
    )
    
    for position, (name, elo) in enumerate(sorted_players, start=1):
        print(f"{' ' * 2}{position:<8} | {name:<20} | {elo:<10}")


print("-"*40)
print("Welcome to Chess Leaderboard")
print("-"*40)
print("1. View Dashboard")
print("2. Enter Challenge Mode ")
print("0. Exit the Application")

while True:
    choice = input("\nPlease enter you choice: ")
    if choice  == "0":
        print("Exiting the program...")
        break
    if choice  == "1":
        leaderBoard(players)
        continue
    elif choice  == "2":
        challenge()
    else:
        print("Invalid Choice. Please Try Again.")
        continue