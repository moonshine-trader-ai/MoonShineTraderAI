class SpreadAnalyzer:

    def __init__(self):

        self.max_spread = {
            "EURUSD": 2.0,
            "GBPUSD": 3.0,
            "USDJPY": 2.0,
            "XAUUSD": 30.0
        }

    def analyze(self, symbol, spread):

        limit = self.max_spread.get(symbol, 2.0)

        if spread <= limit:
            return "SPREAD_OK", 10

        return "SPREAD_TOO_HIGH", 0