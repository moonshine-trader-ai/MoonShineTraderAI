class CandlestickAnalyzer:

    def analyze(self, open_price, high, low, close):

        body = abs(close - open_price)
        candle_range = high - low

        if candle_range == 0:
            return "NO_PATTERN", 0

        # Bullish Engulfing (simplified for now)
        if close > open_price and body > (candle_range * 0.6):
            return "BULLISH_ENGULFING", 20

        # Bearish Engulfing (simplified for now)
        if close < open_price and body > (candle_range * 0.6):
            return "BEARISH_ENGULFING", 20

        # Doji
        if body < (candle_range * 0.1):
            return "DOJI", 5

        return "NO_PATTERN", 0