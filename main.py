# main.py
import os
from dotenv import load_dotenv
from utils.trading_logic import run_trading_bot

# Load environment variables from .env
load_dotenv()

if __name__ == "__main__":
    try:
        print("Starting trading bot...")
        run_trading_bot()
        print("Trading bot run completed.")
    except Exception as e:
        print(f"Error running trading bot: {e}")
