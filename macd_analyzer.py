class MACDAnalyzer:

    def calculate_ema(self, prices, period):

        if len(prices) < period:
            return None

        multiplier = 2 / (period + 1)

        ema = sum(prices[:period]) / period

        for price in prices[period:]:
            ema = (price - ema) * multiplier + ema

        return ema

    def analyze(self, prices):

        ema12 = self.calculate_ema(prices, 12)
        ema26 = self.calculate_ema(prices, 26)

        if ema12 is None or ema26 is None:
            return "NOT_ENOUGH_DATA", 0, None

        macd = ema12 - ema26

        if macd > 0.0005:
            return "STRONG_BULLISH_MACD", 20, round(macd, 5)

        elif macd > 0:
            return "BULLISH_MACD", 15, round(macd, 5)

        elif macd < -0.0005:
            return "STRONG_BEARISH_MACD", 20, round(macd, 5)

        elif macd < 0:
            return "BEARISH_MACD", 15, round(macd, 5)

        return "NEUTRAL_MACD", 5, round(macd, 5)