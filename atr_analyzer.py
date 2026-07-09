class ATRAnalyzer:

    def calculate(self, rates, period=14):

        if len(rates) < period + 1:
            return 0.0

        true_ranges = []

        for i in range(1, len(rates)):

            high = float(rates[i]["high"])
            low = float(rates[i]["low"])
            previous_close = float(rates[i - 1]["close"])

            tr = max(
                high - low,
                abs(high - previous_close),
                abs(low - previous_close)
            )

            true_ranges.append(tr)

        atr = sum(true_ranges[-period:]) / period

        return round(atr, 5)