class EMAAnalyzer:

    def calculate(self, prices, period):

        if len(prices) < period:
            return None

        multiplier = 2 / (period + 1)

        ema = sum(prices[:period]) / period

        for price in prices[period:]:
            ema = (price - ema) * multiplier + ema

        return round(ema, 5)

    def analyze(self, prices):

        ema20 = self.calculate(prices, 20)
        ema50 = self.calculate(prices, 50)
        ema200 = self.calculate(prices, 200)

        if ema20 is None or ema50 is None or ema200 is None:
            return "NOT_ENOUGH_DATA", 0, ema20, ema50, ema200

        if ema20 > ema50 > ema200:
            return "STRONG_BULLISH_EMA", 25, ema20, ema50, ema200

        elif ema20 < ema50 < ema200:
            return "STRONG_BEARISH_EMA", 25, ema20, ema50, ema200

        elif ema20 > ema50:
            return "BULLISH_EMA", 15, ema20, ema50, ema200

        elif ema20 < ema50:
            return "BEARISH_EMA", 15, ema20, ema50, ema200

        return "SIDEWAYS_EMA", 5, ema20, ema50, ema200