"""
weather.py - Calculates the day with the smallest temperature spread.
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

# Path resolution: checks ../data/weather.dat, ./data/weather.dat, or ./weather.dat
BASE_DIR = SRC_DIR.parent
DEFAULT_DATA_PATH = BASE_DIR / "data" / "weather.dat"
DATA_FILE = str(DEFAULT_DATA_PATH if DEFAULT_DATA_PATH.exists() else Path("weather.dat"))

# Named variables for column positions
DAY_COL = 0
MAX_TEMP_COL = 1
MIN_TEMP_COL = 2


def main(filepath=DATA_FILE):
    weather_calculator = Calculator(
        filepath=filepath,
        label_col=DAY_COL,
        val1_col=MAX_TEMP_COL,
        val2_col=MIN_TEMP_COL,
        filter_fn=lambda day: day.isdigit()  # Ensures only valid day numbers are processed (excludes 'mo')
    )

    day_num, min_temp_spread = weather_calculator.execute()
    print(f"Day with smallest temperature spread: Day {day_num} (spread: {min_temp_spread:.1f})")
    return day_num, min_temp_spread


if __name__ == "__main__":
    main()
