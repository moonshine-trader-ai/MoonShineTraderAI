class SupportResistanceAnalyzer:

    def analyze(self, current_price, prices):

        support = min(prices)
        resistance = max(prices)

        score = 0
        reason = "NO_SETUP"

        tolerance = 0.0005

        if abs(current_price - support) <= tolerance:
            score = 20
            reason = "NEAR_SUPPORT"

        elif abs(current_price - resistance) <= tolerance:
            score = 20
            reason = "NEAR_RESISTANCE"

        return support, resistance, score, reason