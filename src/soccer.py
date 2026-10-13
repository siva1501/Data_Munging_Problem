"""
soccer.py - Calculates the soccer team with the smallest difference in for/against goals.
"""
import os
import sys
from pathlib import Path

# Ensure src directory is in sys.path
SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

try:
    from src.calculator import Calculator
except ModuleNotFoundError:
    from calculator import Calculator

# Path resolution: checks ../data/football.dat, ./data/football.dat, or ./football.dat
BASE_DIR = SRC_DIR.parent
DEFAULT_DATA_PATH = BASE_DIR / "data" / "football.dat"
DATA_FILE = str(DEFAULT_DATA_PATH if DEFAULT_DATA_PATH.exists() else Path("football.dat"))

# Named variables for column positions (avoiding magic numbers like 6 directly)
TEAM_COL = 1
GOALS_FOR_COL = 6
GOALS_AGAINST_COL = 8


def main(filepath=DATA_FILE):
    soccer_calculator = Calculator(
        filepath=filepath,
        label_col=TEAM_COL,
        val1_col=GOALS_FOR_COL,
        val2_col=GOALS_AGAINST_COL
    )

    team_name, min_goal_diff = soccer_calculator.execute()
    print(f"Team with smallest goal difference: {team_name} (difference: {min_goal_diff:.0f})")
    return team_name, min_goal_diff


if __name__ == "__main__":
    main()
