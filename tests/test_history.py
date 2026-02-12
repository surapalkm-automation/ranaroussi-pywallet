import unittest
from unittest.mock import MagicMock
import pandas as pd
from yfinance.scrapers.history import PriceHistory

class TestPriceHistoryNull(unittest.TestCase):
    def setUp(self):
        self.mock_data = MagicMock()
        self.ticker = "AAPL"
        self.tz = "UTC"

    def test_null_json_response(self):
        # Scenario: data.json() returns None
        mock_response = MagicMock()
        mock_response.text = "null"
        mock_response.json.return_value = None
        self.mock_data.get.return_value = mock_response

        ph = PriceHistory(self.mock_data, self.ticker, self.tz)
        
        # This should NOT raise TypeError anymore
        try:
            df = ph.history(period="1d")
            self.assertTrue(df.empty)
        except TypeError as e:
            self.fail(f"Raised TypeError: {e}")

    def test_null_chart_response(self):
        # Scenario: data.json() returns {'chart': None}
        mock_response = MagicMock()
        mock_response.text = '{"chart": null}'
        mock_response.json.return_value = {'chart': None}
        self.mock_data.get.return_value = mock_response

        ph = PriceHistory(self.mock_data, self.ticker, self.tz)
        
        # This should NOT crash
        try:
            df = ph.history(period="1d")
            self.assertTrue(df.empty)
        except TypeError as e:
            self.fail(f"Raised TypeError: {e}")

if __name__ == '__main__':
    unittest.main()
