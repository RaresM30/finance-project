import json
import unittest
from unittest.mock import patch

import yfinance

from domain.asset.asset import Asset


class TestForAssets(unittest.TestCase):

    def test_ticker(self):
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.ticker, 'tsla')

    def test_units(self):
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.units, 15)

    def test_name(self):
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.name, 'Tesla')

    def test_country(self):
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.country, 'US')

    def test_sector(self):
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.sector, 'Technology')

    @patch('yfinance.Ticker')
    def test_current_price(self, mock_yfinance):
        expected = 170.06
        mock_yfinance.return_value.fast_info = {'lastPrice': expected}
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.current_price, expected)

    @patch('yfinance.Ticker')
    def test_currency(self, mock_yfinance):
        expected = 'USD'
        mock_yfinance.return_value.fast_info = {'currency': expected}
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.currency, expected)

    @patch('yfinance.Ticker')
    def test_closed_price(self, mock_yfinance):
        expected = 161.99
        mock_yfinance.return_value.fast_info = {'previousClose': expected}
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.closed_price, expected)

    @patch('yfinance.Ticker')
    def test_fifty_day_price(self, mock_yfinance):
        expected = 182.44
        mock_yfinance.return_value.fast_info = {'fiftyDayAverage': expected}
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.fifty_day_price, expected)

    @patch('yfinance.Ticker')
    def test_today_low_price(self, mock_yfinance):
        expected = 163.50
        mock_yfinance.return_value.fast_info = {'dayLow': expected}
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.today_low_price, expected)

    @patch('yfinance.Ticker')
    def test_today_high_price(self, mock_yfinance):
        expected = 170.78
        mock_yfinance.return_value.fast_info = {'dayHigh': expected}
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.today_high_price, expected)

    @patch('yfinance.Ticker')
    def test_open_price(self, mock_yfinance):
        expected = 163.97
        mock_yfinance.return_value.fast_info = {'open': expected}
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')
        self.assertEqual(asset.open_price, expected)

    @patch('yfinance.Ticker')
    def test_percentage_diff_when_current_price_is_higher(self, mock_yfinance):
        mock_yfinance.return_value.fast_info = {
            'lastPrice': 100.0,
            'previousClose': 95.0,
        }
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')

        expected = 'The closed 95.0 is 5.26% lower than current 100.0'
        self.assertEqual(asset.percentage_diff, expected)

    @patch('yfinance.Ticker')
    def test_percentage_diff_when_current_price_is_lower(self, mock_yfinance):
        mock_yfinance.return_value.fast_info = {
            'lastPrice': 90.0,
            'previousClose': 95.0,
        }
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')

        expected = 'The closed price 95.0 is 5.3% higher than the current price 90.0'
        self.assertEqual(asset.percentage_diff, expected)

    @patch('yfinance.Ticker')
    def test_percentage_diff_when_current_price_is_same_as_closed_price(self, mock_yfinance):
        mock_yfinance.return_value.fast_info = {
            'lastPrice': 95.0,
            'previousClose': 95.0,
        }
        asset = Asset('tsla', 15, 'Tesla', 'US', 'Technology')

        expected = 'The values are the same'
        self.assertEqual(asset.percentage_diff, expected)



if __name__ == '__main__':
    unittest.main()
