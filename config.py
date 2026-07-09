import MetaTrader5 as mt5

# ===============================
# MoonShine Trader AI Configuration
# ===============================

BOT_NAME = "MoonShine Trader AI"
VERSION = "1.0"

# Markets to scan
SYMBOLS = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "XAUUSD"
]

# MT5 Timeframe
TIMEFRAME = mt5.TIMEFRAME_M5

# Trading Risk
RISK_PERCENT = 1.0
MAX_OPEN_TRADES = 3

# Trade Settings
TAKE_PROFIT_PIPS = 40
STOP_LOSS_PIPS = 20

# Analysis
CANDLES_TO_LOAD = 100
MIN_CANDLES_REQUIRED = 20