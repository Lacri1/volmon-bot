from binance.client import Client
import os

class BinanceClient:
    def __init__(self):
        api_key = os.getenv('BINANCE_API_KEY')
        api_secret = os.getenv('BINANCE_API_SECRET')
        if not api_key or not api_secret:
            print("Error: BINANCE_API_KEY or BINANCE_API_SECRET not found in .env file.")
            # You might want to raise an exception or handle this more gracefully
            exit(1)
        self.client = Client(api_key, api_secret)

    def get_ticker_price(self, symbol: str):
        try:
            info = self.client.get_symbol_ticker(symbol=symbol)
            return info
        except Exception as e:
            raise Exception(f"Error fetching ticker price for {symbol}: {e}")

    def get_klines(self, symbol: str, interval: str, limit: int = 500):
        try:
            # Binance API returns klines as a list of lists
            # Each inner list contains: [open_time, open, high, low, close, volume, close_time, ...] 
            klines = self.client.get_klines(symbol=symbol, interval=interval, limit=limit)
            # We only need the first 6 elements for our chart
            return [k[:6] for k in klines]
        except Exception as e:
            raise Exception(f"Error fetching klines for {symbol} with interval {interval}: {e}")