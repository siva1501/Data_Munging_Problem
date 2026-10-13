"""
calculator.py - Coordinates extraction and analysis to execute the calculation.
"""
try:
    from src.data_extractor import DataExtractor
    from src.data_analyzer import DataAnalyzer
except ModuleNotFoundError:
    from data_extractor import DataExtractor
    from data_analyzer import DataAnalyzer


class Calculator:
    """
    Coordinates DataExtractor and DataAnalyzer to find the item with the minimum difference.
    """

    def __init__(self, filepath, label_col, val1_col, val2_col, diff_fn=None, filter_fn=None):
        # Initializes both collaborating classes with custom parameters
        self.extractor = DataExtractor(
            filepath=filepath,
            label_col=label_col,
            val1_col=val1_col,
            val2_col=val2_col,
            filter_fn=filter_fn
        )
        self.analyzer = DataAnalyzer(diff_fn=diff_fn)

    def execute(self):
        """Extracts data and returns the item with the minimum difference."""
        records = self.extractor.extract()
        return self.analyzer.find_min_diff(records)
