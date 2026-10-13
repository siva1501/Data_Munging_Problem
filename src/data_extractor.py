"""
data_extractor.py - Single Responsibility: Extracts raw data from files.
"""
import inspect


class DataExtractor:
    """Extracts structured records from tabular text files with customizable columns."""

    def __init__(self, filepath, label_col, val1_col, val2_col, filter_fn=None):
        self.filepath = filepath
        self.label_col = label_col
        self.val1_col = val1_col
        self.val2_col = val2_col
        self.filter_fn = filter_fn

    def extract(self):
        """
        Parses the file and extracts valid (label, val1, val2) records.
        Handles non-numeric markers (e.g. '*') and ignores invalid/header rows.
        """
        records = []
        max_col = max(self.label_col, self.val1_col, self.val2_col)

        with open(self.filepath, "r") as f:
            for line in f:
                tokens = line.split()
                if len(tokens) <= max_col:
                    continue

                try:
                    # Clean trailing special characters (e.g. '*' in temperature data)
                    v1 = float(tokens[self.val1_col].rstrip("*"))
                    v2 = float(tokens[self.val2_col].rstrip("*"))
                    label = tokens[self.label_col]
                except ValueError:
                    # Skip headers, separators, or invalid non-numeric rows
                    continue

                if self.filter_fn:
                    sig = inspect.signature(self.filter_fn)
                    if len(sig.parameters) == 1:
                        if not self.filter_fn(label):
                            continue
                    else:
                        if not self.filter_fn(label, v1, v2):
                            continue

                records.append((label, v1, v2))

        return records
