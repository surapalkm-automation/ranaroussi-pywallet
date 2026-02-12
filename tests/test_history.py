import unittest
from unittest.mock import patch
import pandas as pd
# Assuming the package is installed or in python path
from yfinance.scrapers.history import History

class TestHistory(unittest.TestCase):
    def test_history_null_response(self):
        h = History("AAPL")
        
        # Patch the method that returns data to return None
        with patch.object(h, '_download_history_data', return_value=None):
            # This should not raise TypeError after the fix
            try:
                df = h.history()
                # If we reach here, it returned something.
                # After fix, we expect empty DataFrame
                self.assertTrue(df.empty)
            except TypeError as e:
                self.fail(f"Raised TypeError: {e}")
            except Exception as e:
                self.fail(f"Raised unexpected exception: {e}")

    def test_history_null_chart_result(self):
        h = History("AAPL")
        # Patch to return data with null result
        bad_data = {"chart": {"result": None}}
        
        with patch.object(h, '_download_history_data', return_value=bad_data):
            try:
                df = h.history()
                self.assertTrue(df.empty)
            except TypeError as e:
                self.fail(f"Raised TypeError: {e}")

if __name__ == '__main__':
    unittest.main()
