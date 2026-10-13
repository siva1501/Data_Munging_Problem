"""
Version 1: Spike Solution (Kata04: Data Munging)

Goal: "Spike out the first version just make it work."
A spike test explores the problem directly with minimal ceremony,
discovering data formatting quirks, anomalies, and edge cases.

Edge cases discovered during spike:
1. Asterisks in temperature numbers (e.g., '32*', '97*') in weather.dat.
2. Irregular spacing and separator lines (e.g., '-------------------').
3. Column shifting due to '-' separator in football.dat.
4. Summary rows at the end of files (e.g., 'mo' row in weather.dat).
"""
from pathlib import Path

# Resolve data file paths dynamically
BASE_DIR = Path(__file__).resolve().parent
WEATHER_FILE = str(BASE_DIR / "data" / "weather.dat" if (BASE_DIR / "data" / "weather.dat").exists() else BASE_DIR / "weather.dat")
SOCCER_FILE = str(BASE_DIR / "data" / "football.dat" if (BASE_DIR / "data" / "football.dat").exists() else BASE_DIR / "football.dat")


def spike_weather(filepath=WEATHER_FILE):
    min_spread = float("inf")
    result_day = None

    with open(filepath, "r") as f:
        for line in f:
            tokens = line.split()
            # Valid weather data row has at least 3 tokens and the first token is a day number
            if len(tokens) >= 3 and tokens[0].isdigit():
                try:
                    day = tokens[0]
                    max_temp = float(tokens[1].rstrip("*"))
                    min_temp = float(tokens[2].rstrip("*"))
                    spread = abs(max_temp - min_temp)

                    if spread < min_spread:
                        min_spread = spread
                        result_day = day
                except ValueError:
                    continue

    return result_day, min_spread


def spike_soccer(filepath=SOCCER_FILE):
    min_diff = float("inf")
    result_team = None

    with open(filepath, "r") as f:
        for line in f:
            tokens = line.split()
            # Valid row starts with rank (e.g., '1.') and has team, goals for, goals against
            # In football.dat: tokens[1] is Team, tokens[6] is F, tokens[8] is A
            if len(tokens) >= 9:
                try:
                    team = tokens[1]
                    goals_for = float(tokens[6])
                    goals_against = float(tokens[8])
                    diff = abs(goals_for - goals_against)

                    if diff < min_diff:
                        min_diff = diff
                        result_team = team
                except ValueError:
                    continue

    return result_team, min_diff


if __name__ == "__main__":
    day, spread = spike_weather()
    print(f"[Spike] Weather - Day with smallest temperature spread: Day {day} (spread: {spread:.1f})")

    team, diff = spike_soccer()
    print(f"[Spike] Soccer  - Team with smallest goal difference: {team} (difference: {diff:.0f})")
