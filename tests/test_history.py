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
        
        # This should currently raise TypeError
        try:
            ph.history(period="1d")
        except TypeError as e:
            print(f"\nCaught expected TypeError: {e}")
            pass
        except Exception as e:
            self.fail(f"Caught unexpected exception: {e}")
        else:
            self.fail("TypeError not raised")

    def test_null_chart_response(self):
        # Scenario: data.json() returns {'chart': None}
        mock_response = MagicMock()
        mock_response.text = '{"chart": null}'
        mock_response.json.return_value = {'chart': None}
        self.mock_data.get.return_value = mock_response

        ph = PriceHistory(self.mock_data, self.ticker, self.tz)
        
        # This should crash at data['chart']['result'] -> TypeError
        try:
            ph.history(period="1d")
        except TypeError as e:
            print(f"\nCaught expected TypeError: {e}")
            pass
        except Exception as e:
            self.fail(f"Caught unexpected exception: {e}")
        else:
            self.fail("TypeError not raised")

if __name__ == '__main__':
    unittest.main()
