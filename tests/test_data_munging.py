"""
Unit tests for Data Munging solution.
"""
import unittest
from pathlib import Path

from src.data_extractor import DataExtractor
from src.data_analyzer import DataAnalyzer
from src.calculator import Calculator
from src.weather import main as run_weather
from src.soccer import main as run_soccer


class TestDataMunging(unittest.TestCase):
    def setUp(self):
        self.base_dir = Path(__file__).resolve().parent.parent
        self.weather_file = str(self.base_dir / "data" / "weather.dat")
        self.soccer_file = str(self.base_dir / "data" / "football.dat")

    def test_weather_data_extraction(self):
        extractor = DataExtractor(
            filepath=self.weather_file,
            label_col=0,
            val1_col=1,
            val2_col=2,
            filter_fn=lambda day: day.isdigit()
        )
        records = extractor.extract()
        self.assertEqual(len(records), 30)  # 30 days in June
        # Day 1: Max 88, Min 59
        self.assertEqual(records[0], ("1", 88.0, 59.0))
        # Day 9: Max 86, Min 32* (cleaned to 32.0)
        self.assertEqual(records[8], ("9", 86.0, 32.0))

    def test_soccer_data_extraction(self):
        extractor = DataExtractor(
            filepath=self.soccer_file,
            label_col=1,
            val1_col=6,
            val2_col=8
        )
        records = extractor.extract()
        self.assertEqual(len(records), 20)  # 20 teams in Premier League
        # Team 1: Arsenal, F 79, A 36
        self.assertEqual(records[0], ("Arsenal", 79.0, 36.0))

    def test_data_analyzer_min_diff(self):
        analyzer = DataAnalyzer()
        dummy_data = [
            ("Alpha", 10.0, 5.0),   # diff: 5
            ("Beta", 20.0, 18.0),   # diff: 2
            ("Gamma", 15.0, 14.0),  # diff: 1
        ]
        label, min_diff = analyzer.find_min_diff(dummy_data)
        self.assertEqual(label, "Gamma")
        self.assertEqual(min_diff, 1.0)

    def test_weather_result(self):
        day, spread = run_weather(self.weather_file)
        self.assertEqual(day, "14")
        self.assertAlmostEqual(spread, 2.0)

    def test_soccer_result(self):
        team, diff = run_soccer(self.soccer_file)
        self.assertEqual(team, "Aston_Villa")
        self.assertAlmostEqual(diff, 1.0)


if __name__ == "__main__":
    unittest.main()
