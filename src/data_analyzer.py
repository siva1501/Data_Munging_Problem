"""
data_analyzer.py - Single Responsibility: Analyzes data records to find minimum differences.
"""


class DataAnalyzer:
    """Calculates differences between numeric values and determines the minimum."""

    def __init__(self, diff_fn=None):
        # Allow customization of the difference calculation (defaults to absolute difference)
        self.diff_fn = diff_fn or (lambda v1, v2: abs(v1 - v2))

    def find_min_diff(self, records):
        """
        Finds the record with the minimum difference.

        :param records: List of (label, val1, val2) tuples
        :return: Tuple of (label, min_diff)
        """
        if not records:
            return None, None

        min_record = min(records, key=lambda row: self.diff_fn(row[1], row[2]))
        min_diff = self.diff_fn(min_record[1], min_record[2])
        return min_record[0], min_diff
