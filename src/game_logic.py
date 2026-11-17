import random

game_stats = {"wins": 0, "losses": 0, "ties": 0}

rock_paper_scissor = ["rock", "paper", "scissors"]


def get_computer_choice():
    return random.choice(rock_paper_scissor)


def get_player_choice():
    while True:
        player_input = (
            input("player must choose: rock, paper, or scissors? ").lower().strip()
        )
        if player_input not in rock_paper_scissor:
            print("please select rock, paper, or scissors")
            continue
        else:
            return player_input


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif player_choice == "rock" and computer_choice == "scissors":
        return "win"
    elif player_choice == "paper" and computer_choice == "rock":
        return "win"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "win"
    else:
        return "loss"


def update_stats(result):
    if result == "win":
        game_stats["wins"] += 1
    elif result == "loss":
        game_stats["losses"] += 1
    elif result == "tie":
        game_stats["ties"] += 1
    else:
        print("not a valid entry")
        raise ValueError


def play_round():
    player_choice = get_player_choice()
    print(f"you chose: {player_choice}")
    computer_choice = get_computer_choice()
    print(f"computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(f"result: {result}")
    return update_stats(result)


def get_win_rate():
    total_games = game_stats["wins"] + game_stats["losses"] + game_stats["ties"]
    if total_games == 0:
        return 0
    win_rate = game_stats["wins"] / total_games * 100
    return round(win_rate)
