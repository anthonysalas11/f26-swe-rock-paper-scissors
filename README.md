# Rock paper scissor CLI game

**The project brief is in [PROJECT.md](./PROJECT.md).** Start there.

This file is yours to write. When your project works, replace everything here
with a description of what you built: what it does, how to run it, and a usage
example. Write it for someone who has never seen your project before.

For an example of what a finished one looks like, see the
[Task Manager Case Study](https://github.com/The-Marcy-Lab-School/swe-casestudy-1-cli-task-manager),
which is a working Python CLI app with investigation questions to work
through.


# Rock Paper Scissors CLI Game

## About

For my Mod 1 project, I decided to build a Rock Paper Scissors game using Python. The game allows you to play against the computer by choosing rock, paper, or scissors. The computer randomly picks its choice, and the program determines who wins.

I also added a stats feature that keeps track of how many games you win, lose, or tie. You can check your stats while playing and see your final stats when you exit.

## How to Run

1. Clone the repository:

   ```bash
   git clone 
   ```

2. Go into the project folder:

   ```bash
   cd f26-swe-rock-paper-scissors
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the game:

   ```bash
   python3 src/main.py
   ```

## How to Play

Once the game starts, you will see a menu with three options:

1. Play Round
2. View Stats
3. Exit

Choose an option by entering 1, 2, or 3.

When playing a round, enter rock, paper, or scissors when prompted. The computer will randomly choose its move, and the game will tell you who won.

## Game Rules

- Rock beats scissors.
- Scissors beats paper.
- Paper beats rock.
- If both players choose the same move, it's a tie.

## Features

- Play against the computer.
- Random computer choices.
- Tracks wins, losses, and ties.
- Calculates win rate.
- View game statistics.
- Checks for incorrect input.
- Displays final statistics when exiting.

## Project Structure

```text
src/
├── main.py
├── menu.py
└── game_logic.py
```

- `main.py` starts the application.
- `menu.py` handles the menu and statistics.
- `game_logic.py` contains the functions for playing the game and keeping score.
