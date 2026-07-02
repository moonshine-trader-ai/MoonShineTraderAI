class TrendAnalyzer:

    def analyze(self, price, ma5, ma10):

        if price > ma5 and ma5 > ma10:
            return "STRONG_UPTREND", 25

        elif price > ma10:
            return "WEAK_UPTREND", 15

        elif price < ma5 and ma5 < ma10:
            return "STRONG_DOWNTREND", 25

        elif price < ma10:
            return "WEAK_DOWNTREND", 15

        else:
            return "SIDEWAYS", 5