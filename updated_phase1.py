from functools import wraps

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
    "Gukesh D": 813,
    "Magnus Carlsen": 805
}

# Game History
game_logs = []

# Rating Decorator
def rating(func):
    @wraps(func)
    def wrapper(challenger, defender, result):

        # Store ratings before the game
        challenger_before = players[challenger]
        defender_before = players[defender]

        # Execute the original function
        game_result = func(challenger, defender, result)

        # Update ratings based on game result
        if game_result == "win":
            players[challenger] += 10
            players[defender] -= 10

        elif game_result == "loss":
            players[challenger] -= 10
            players[defender] += 10

        # Store ratings after the game
        challenger_after = players[challenger]
        defender_after = players[defender]

        # Store game details
        game_logs.append({
            "challenger": challenger,
            "defender": defender,
            "result": game_result,
            "challenger_rating_before": challenger_before,
            "challenger_rating_after": challenger_after,
            "defender_rating_before": defender_before,
            "defender_rating_after": defender_after,
            "rating_changes": {
                "challenger": challenger_after - challenger_before,
                "defender": defender_after - defender_before
            }
        })

        return game_result

    return wrapper


# Game Result Function
@rating
def game_result(challenger, defender, result):

    if result in ["win", "w"]:
        return "win"

    elif result in ["loss", "l"]:
        return "loss"

    elif result in ["draw", "d"]:
        return "draw"


# Challenge Function
def challenge():

    print("\n" + "-" * 40)
    print("WELCOME TO CHALLENGE MODE:")
    print("-" * 40)
    print("NOTE: You can challenge only players whose rating is higher than yours.")

    while True:

        challenger = input("\nEnter your name (Challenger): ").strip()
        defender = input("Enter the player name you want to challenge (Defender): ").strip()

        # Check player availability
        if challenger not in players or defender not in players:
            print("\nERROR: Player does not exist. Please try again.")
            continue

        # Prevent self-challenge
        if challenger == defender:
            print("\nERROR: You cannot challenge yourself.")
            continue

        # Check rating eligibility
        if players[defender] <= players[challenger]:
            print("\nNOTE: CHALLENGE DENIED.")
            print("Please challenge a player whose rating is greater than yours.")
            continue

        print("\nNOTE: CHALLENGE ACCEPTED.")

        print(f"\nChallenger Rating Before Game: {players[challenger]}")
        print(f"Defender Rating Before Game: {players[defender]}")

        # Get valid game result
        while True:

            result = input("\nPlease enter the game result (win/loss/draw): ").strip().lower()

            if result in ["win", "w", "loss", "l", "draw", "d"]:
                break

            print("ERROR: Invalid game result. Please try again.")

        # Execute decorated function
        final_result = game_result(challenger, defender, result)

        if final_result == "win":
            print("\nThe Challenger has won the game.")

        elif final_result == "loss":
            print("\nThe Defender has won the game.")

        else:
            print("\nGame has resulted in a draw. No changes in player ratings.")

        print(f"\nChallenger Rating After Game: {players[challenger]}")
        print(f"Defender Rating After Game: {players[defender]}")

        break


# Leaderboard Display
def leaderBoard(players):

    if not players:
        print("No Players to display.")
        return

    print("\n" + "-" * 45)
    print("  Current Leader Board")
    print("-" * 45)
    print(f"  {'Rank':<8} | {'Player Name':<20} | {'Rating':<10}")
    print("-" * 45)

    sorted_players = sorted(
        players.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for position, (name, elo) in enumerate(sorted_players, start=1):
        print(f"  {position:<8} | {name:<20} | {elo:<10}")


# Display Game Logs
def view_game_logs():

    if not game_logs:
        print("\nNo game history available.")
        return

    print("\n" + "-" * 60)
    print("GAME HISTORY")
    print("-" * 60)

    for position, game in enumerate(game_logs, start=1):

        print(f"\nGame #{position}")
        print(f"Challenger: {game['challenger']}")
        print(f"Defender: {game['defender']}")
        print(f"Result: {game['result'].upper()}")

        print(f"Challenger Rating: {game['challenger_rating_before']} -> {game['challenger_rating_after']}")
        print(f"Defender Rating: {game['defender_rating_before']} -> {game['defender_rating_after']}")

        print(f"Rating Changes: {game['rating_changes']}")


# Main Application
print("-" * 40)
print("Welcome to Chess Leaderboard")
print("-" * 40)

while True:

    print("\n1. View Leader Board")
    print("2. Enter Challenge Mode")
    print("3. View Game History")
    print("0. Exit the Application")

    choice = input("\nPlease enter your choice: ").strip()

    if choice == "0":
        print("Exiting the program...")
        break

    elif choice == "1":
        leaderBoard(players)

    elif choice == "2":
        challenge()

    elif choice == "3":
        view_game_logs()

    else:
        print("Invalid Choice. Please Try Again.")
