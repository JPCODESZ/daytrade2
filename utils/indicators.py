# utils/indicators.py
import pandas_ta as ta


def apply_indicators(df):
    """
    Adds technical indicators (RSI, MACD, ATR) to the given DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame with OHLCV data.

    Returns:
        pd.DataFrame: The DataFrame with new indicator columns appended.
    """
    df.ta.rsi(length=14, append=True)
    df.ta.macd(append=True)
    df.ta.atr(length=14, append=True)
    return df

