class CandlestickAnalyzer:

    def analyze(self, open_price, high, low, close):

        body = abs(close - open_price)
        candle_range = high - low

        if candle_range <= 0:
            return "NO_PATTERN", 0

        upper_wick = high - max(open_price, close)
        lower_wick = min(open_price, close) - low

        # Strong Bullish Candle
        if close > open_price and body >= candle_range * 0.6:
            return "BULLISH_ENGULFING", 20

        # Strong Bearish Candle
        if close < open_price and body >= candle_range * 0.6:
            return "BEARISH_ENGULFING", 20

        # Hammer
        if lower_wick > body * 2 and upper_wick < body:
            return "HAMMER", 15

        # Shooting Star
        if upper_wick > body * 2 and lower_wick < body:
            return "SHOOTING_STAR", 15

        # Doji
        if body <= candle_range * 0.1:
            return "DOJI", 5

        return "NO_PATTERN", 0