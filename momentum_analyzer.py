class MomentumAnalyzer:

    def analyze(self, rsi):

        if rsi >= 70:
            return "STRONG_MOMENTUM", 20

        elif rsi >= 55:
            return "GOOD_MOMENTUM", 15

        elif rsi >= 45:
            return "NEUTRAL_MOMENTUM", 8

        else:
            return "WEAK_MOMENTUM", 0