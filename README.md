# Kata04: Data Munging

A clean, object-oriented, and SOLID-compliant Python implementation of the [CodeKata Kata04: Data Munging](http://codekata.com/kata/kata04-data-munging) challenge.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Directory Structure](#directory-structure)
3. [Virtual Environment Setup](#virtual-environment-setup)
4. [Running the Solution](#running-the-solution)
5. [Running Unit Tests](#running-unit-tests)
6. [Design & Architecture (OOP & SOLID)](#design--architecture-oop--solid)
   - [Version 1: The Spike](#version-1-the-spike)
   - [Version 2: Modular OOP Architecture](#version-2-modular-oop-architecture)
7. [Results](#results)

---

## Project Overview

The Data Munging problem consists of two real-world datasets:
- **Part 1 (Weather Data)**: In `data/weather.dat`, find the day number (column 1) with the smallest temperature spread (`MxT - MnT`).
- **Part 2 (Soccer League Table)**: In `data/football.dat`, find the team name with the smallest absolute difference in goals scored ('F') and goals conceded ('A').
- **Part 3 (DRY Fusion & OOP)**: Factor out all shared parsing, data manipulation, and calculation logic into reusable classes while avoiding magic numbers.

---

## Directory Structure

```text
Data Munging Problem/
├── data/
│   ├── football.dat          # Premier league results dataset
│   └── weather.dat           # Morristown daily weather dataset
├── src/
│   ├── __init__.py           # Package marker
│   ├── data_extractor.py     # Class: DataExtractor (extracts and sanitizes records)
│   ├── data_analyzer.py      # Class: DataAnalyzer (computes min difference)
│   ├── calculator.py         # Class: Calculator (coordinates extractor & analyzer)
│   ├── weather.py            # Executes weather analysis using named column variables
│   └── soccer.py             # Executes soccer analysis using named column variables
├── tests/
│   └── test_data_munging.py  # Comprehensive unit tests
├── spike.py                  # Version 1 quick spike prototype
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore rules for venv, caches, and IDE files
└── README.md                 # Project documentation
```

---

## Virtual Environment & Dependency Setup

You can use modern **`uv`** (recommended) or standard **`python3 -m venv`**.

### Option A: Using `uv` (Recommended)

1. **Create virtual environment and sync packages**:
   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```
   Or simply let `uv` manage execution automatically:
   ```bash
   uv sync
   ```

2. **Run scripts with `uv`**:
   ```bash
   # Weather analysis
   uv run python src/weather.py

   # Soccer analysis
   uv run python src/soccer.py

   # Run tests
   uv run pytest
   ```

---

### Option B: Using Standard `python3 -m venv`

1. **Create and activate**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run scripts**:
   ```bash
   python3 src/weather.py
   python3 src/soccer.py
   python3 -m unittest discover tests
   ```

---

## Running the Solution

From the root directory:

### Run Weather Analysis
```bash
python3 src/weather.py
```
**Output:**
```text
Day with smallest temperature spread: Day 14 (spread: 2.0)
```

### Run Soccer Analysis
```bash
python3 src/soccer.py
```
**Output:**
```text
Team with smallest goal difference: Aston_Villa (difference: 1)
```

### Run the Version 1 Spike
```bash
python3 spike.py
```

---

## Running Unit Tests

Run the test suite via Python's built-in `unittest` runner or `pytest`:

```bash
# Using unittest
python3 -m unittest discover tests

# Using pytest (if installed from requirements.txt)
pytest
```

---

## Design & Architecture (OOP & SOLID)

### Version 1: The Spike
A **spike** is an exploratory prototype designed to explore problem complexity and uncover edge cases without spending time on design overhead.

**Edge cases uncovered during the spike:**
1. **Trailing Asterisks (`*`)**: Certain temperature numbers contain asterisks (e.g. `32*` on day 9 and `97*` on day 26). These must be stripped before float conversion.
2. **Column Shifting**: In `football.dat`, the dash separator `-` between goals for and against is a distinct whitespace token, placing column `F` at index 6 and `A` at index 8.
3. **Non-Data Lines**: Table header rows, separator lines (`---------------------`), and summary averages (the `mo` row in weather data) must be ignored safely.

---

### Version 2: Modular OOP Architecture (5 Core Files)

The second version organizes responsibilities cleanly according to SOLID principles:

| File | Class / Module | SOLID Principle Applied |
| :--- | :--- | :--- |
| `src/data_extractor.py` | `DataExtractor` | **Single Responsibility (SRP)**: Handles file reading, token splitting, string cleanup (`*`), and line filtering. Open for custom filter predicates. |
| `src/data_analyzer.py` | `DataAnalyzer` | **Open/Closed Principle (OCP)**: Computes the minimum difference over records. Accepts an interchangeable difference function (`diff_fn`). |
| `src/calculator.py` | `Calculator` | **Dependency Inversion / Facade**: Coordinates `DataExtractor` and `DataAnalyzer` to execute the full pipeline. |
| `src/weather.py` | Script / Runner | Uses named variables (`DAY_COL`, `MAX_TEMP_COL`, `MIN_TEMP_COL`) rather than magic numbers. Excludes summary lines. |
| `src/soccer.py` | Script / Runner | Uses named variables (`TEAM_COL`, `GOALS_FOR_COL`, `GOALS_AGAINST_COL`). Does **not** pass `6` directly. |

---

## Results

| Problem | Winner / Subject | Metric | Value |
| :--- | :--- | :--- | :--- |
| **Weather** (`weather.dat`) | **Day 14** | Minimum Temperature Spread | **2.0** (61 - 59) |
| **Soccer** (`football.dat`) | **Aston_Villa** | Smallest Goal Difference | **1** (\|46 - 47\|) |
