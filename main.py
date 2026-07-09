from bot_engine import BotEngine
from mt5_data import MT5Data

symbols = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "XAUUSD"
]

mt5 = MT5Data()

markets = {}

for symbol in symbols:

    rates_m5 = mt5.get_rates(symbol, timeframe="M5", candles=250)
    rates_m15 = mt5.get_rates(symbol, timeframe="M15", candles=250)
    rates_h1 = mt5.get_rates(symbol, timeframe="H1", candles=250)

    if (
        len(rates_m5) < 200 or
        len(rates_m15) < 200 or
        len(rates_h1) < 200
    ):
        print(f"Not enough data for {symbol}")
        continue

    spread = mt5.get_spread(symbol)

    markets[symbol] = {

        "rates": rates_m15,

        "prices": [
            float(candle["close"])
            for candle in rates_m15
        ],

        "spread": spread,

        "m5_prices": [
            float(candle["close"])
            for candle in rates_m5
        ],

        "m15_prices": [
            float(candle["close"])
            for candle in rates_m15
        ],

        "h1_prices": [
            float(candle["close"])
            for candle in rates_h1
        ]
    }

bot = BotEngine()

results = bot.run(markets)

print("\n========== MOONSHINE TRADER AI ==========\n")

for trade in results:

    print("-----------------------------------")
    print("Symbol      :", trade["symbol"])
    print("Decision    :", trade["decision"])
    print("Buy Score   :", trade["buy_score"])
    print("Sell Score  :", trade["sell_score"])
    print("Final Score :", trade["score"])
    print("Confidence  :", trade["confidence"])
    print("ATR         :", trade["atr"])

    print("Entry       :", trade["entry"])
    print("Stop Loss   :", trade["stop_loss"])
    print("Take Profit :", trade["take_profit"])

    print("Trade OK    :", trade["trade_allowed"])

    print("Reasons:")

    for reason in trade["reasons"]:
        print(" ", reason)

print("\n=========================================\n")

bot.report()

mt5.shutdown()