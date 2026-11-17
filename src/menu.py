from game_logic import game_stats, get_win_rate, play_round


def view_stats():
    total_games = game_stats["wins"] + game_stats["losses"] + game_stats["ties"]
    print("current statistics:")
    print(f"Games won: {game_stats['wins']}")
    print(f"Games lost: {game_stats['losses']}")
    print(f"Game tied: {game_stats['ties']}")
    print(f"Total games: {total_games}")
    print(f"Win rate: {get_win_rate()}%")


def show_menu():
    while True:
        print("1: play round")
        print("2: view stats")
        print("3: exit")
        users_choice = input("choose actions (1-3) player").strip()
        if users_choice == "1":
            play_round()
        elif users_choice == "2":
            view_stats()
        elif users_choice == "3":
            print("goodbye player 🤣")
            view_stats()
            break
        else:
            print("invalid choice please select 1-3")
