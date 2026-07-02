class ATRAnalyzer:

    def calculate(self, highs, lows, closes, period=14):

        if len(highs) != len(lows):
            return None

        if len(highs) != len(closes):
            return None

        if len(highs) <= period:
            return None

        true_ranges = []

        for i in range(1, len(highs)):

            high_low = highs[i] - lows[i]

            high_close = abs(highs[i] - closes[i - 1])

            low_close = abs(lows[i] - closes[i - 1])

            true_range = max(
                high_low,
                high_close,
                low_close
            )

            true_ranges.append(true_range)

        atr = sum(true_ranges[:period]) / period

        for tr in true_ranges[period:]:
            atr = ((atr * (period - 1)) + tr) / period

        return round(atr, 5)