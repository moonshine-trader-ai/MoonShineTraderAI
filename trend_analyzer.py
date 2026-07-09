class TrendAnalyzer:

    def analyze(self, price, ma5, ma10):

        difference = abs(ma5 - ma10)

        # Strong Uptrend
        if price > ma5 and ma5 > ma10 and difference > 0.0005:
            return "STRONG_UPTREND", 25

        # Weak Uptrend
        elif price > ma10 and ma5 >= ma10:
            return "WEAK_UPTREND", 15

        # Strong Downtrend
        elif price < ma5 and ma5 < ma10 and difference > 0.0005:
            return "STRONG_DOWNTREND", 25

        # Weak Downtrend
        elif price < ma10 and ma5 <= ma10:
            return "WEAK_DOWNTREND", 15

        # Sideways Market
        return "SIDEWAYS", 5