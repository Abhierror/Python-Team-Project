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
    print("WELCOME TO CHALLENGE MODE:")
    print("NOTE: You can Challenge only the player whose rating is more than yours.")

    # take the player and challenger name by the player who is challenging
    challenger = input("Enter you name (Challenger): ")
    defender = input("Enter the player name you want to challenge (Defender): ")

    # Check if both the players are available in the player dictionary
    while True:
        if challenger in players and defender in players:

            # Check is the the challenger rating is less than defender rating
            if players[defender] > players[challenger]:
                print("Challenge Accepted.")

                # Display Both Challenger's and Defender's Rating before the Challenge Game
                print(f"Challenger Rating Before challenge game: {players[challenger]}")
                print(f"Defender Rating Before challenge game: {players[defender]}")

                # Main challenge logic which determines the players ratings
                game_result = None

                if game_result in ["Win", "win", "Won", "won", "w", "W", 1, True]:
                    print("The Challenger has won the game.")
                    players[challenger] += 10
                    players[defender] -= 10

                    # Display Both Challenger's and Defender's Rating after the Challenge Game
                    print(f"Challenger Rating After challenge game: {players[challenger]}")
                    print(f"Defender Rating After challenge game: {players[defender]}")

                elif game_result in ["Loss", "loss", "lost", "Lost", "l", "L", 0, False]:
                    print("The Defender has won the game.")
                    players[challenger] -= 10
                    players[defender] += 10
                
                    # Display Both Challenger's and Defender's Rating after the Challenge Game
                    print(f"Challenger Rating After challenge game: {players[challenger]}")
                    print(f"Defender Rating After challenge game: {players[defender]}")

                elif game_result in ["Draw", "draw", "d", "D"]:
                    print("Game has resulted in a draw. No changes in player ratings.")
                
                    # Display Both Challenger's and Defender's Rating after the Challenge Game
                    print(f"Challenger Rating After challenge game: {players[challenger]}")
                    print(f"Defender Rating After challenge game: {players[defender]}")
            
            else:
                print("Challenge Denied.")
                print("Please challenge a player whose rating is greater than yours.")
        else:
            print(f"Player '{challenger}' or '{defender}' doesn't exits, please try again")
    

# Leader Board Display 
def leaderBoard(players):
    if players < 1:
        print("No Players to display")
    else:
        print("Current Leader Board")
        print("-"*40)
        print(f"{'Rank':<8} | {'Player Name':<20} | {'Rating':<10}")
        print("-"*40)
        
        sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
        
        for position, (name, elo) in enumerate(sorted_players, start=1):
            print(f"{position:<8} | {name:<20} | {elo:<10}")


print("Welcome to Chess Leaderboard")
print("-"*40)
print("1. View Dashboard")
print("2. Enter Challenge Mode: ")
print("0. Exit the Application")
while True:
    choice = int(input("Enter you choice: "))
    if choice == 0:
        print("Exiting the program...")
    if choice == 1:
        leaderBoard()
    elif choice == 2:
        challenge()
    else:
        print("Invalid Choice. Please Enter Valid Choice from the above menu.")
