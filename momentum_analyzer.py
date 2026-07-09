class MomentumAnalyzer:

    def analyze(self, rsi):

        # Overbought
        if rsi >= 70:
            return "STRONG_BULLISH_MOMENTUM", 20

        # Bullish
        elif rsi >= 55:
            return "GOOD_BULLISH_MOMENTUM", 15

        # Neutral
        elif rsi >= 45:
            return "NEUTRAL_MOMENTUM", 8

        # Bearish
        elif rsi >= 30:
            return "GOOD_BEARISH_MOMENTUM", 15

        # Oversold
        else:
            return "STRONG_BEARISH_MOMENTUM", 20