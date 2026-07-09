class SupportResistanceAnalyzer:

    def analyze(self, symbol, current_price, prices):

        support = min(prices)
        resistance = max(prices)

        score = 0
        reason = "NO_SETUP"

        # Symbol-specific tolerance
        tolerance = {
            "EURUSD": 0.0005,
            "GBPUSD": 0.0005,
            "USDJPY": 0.05,
            "XAUUSD": 2.0
        }.get(symbol, 0.0005)

        if abs(current_price - support) <= tolerance:
            score = 20
            reason = "NEAR_SUPPORT"

        elif abs(current_price - resistance) <= tolerance:
            score = 20
            reason = "NEAR_RESISTANCE"

        return support, resistance, score, reason