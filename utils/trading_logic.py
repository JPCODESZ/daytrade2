
# utils/trading_logic.py
import os
import pandas as pd
import alpaca_trade_api as tradeapi
from utils.indicators import apply_indicators

API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("BASE_URL")

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def run_trading_bot():
    symbols = ["AAPL", "TSLA"]  # Example symbols to scan
    for symbol in symbols:
        print(f"\nAnalyzing {symbol}...")
       from alpaca_trade_api.rest import TimeFrame
bars = api.get_bars(symbol, TimeFrame.Minute, limit=100).df
df = bars[bars['symbol'] == symbol]
        df.set_index("t", inplace=True)
        df = apply_indicators(df)

        rsi = df.iloc[-1].get("RSI_14")
        macd = df.iloc[-1].get("MACD_12_26_9")
        atr = df.iloc[-1].get("ATRr_14")

        print(f"RSI: {rsi}, MACD: {macd}, ATR: {atr}")

        if rsi is not None and macd is not None:
            if rsi < 30 and macd > 0:
                place_order(symbol, "buy", qty=1)
            elif rsi > 70 and macd < 0:
                place_order(symbol, "sell", qty=1)

def place_order(symbol, side, qty):
    try:
        print(f"Placing {side} order for {symbol}...")
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force='day'
        )
        print(f"Order placed: {side} {qty} shares of {symbol}")
    except Exception as e:
        print(f"Failed to place order for {symbol}: {e}")
