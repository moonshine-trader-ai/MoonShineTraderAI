class MultiTimeframeAnalyzer:

    def analyze(self, m5_prices, m15_prices, h1_prices):

        def trend(prices):

            ma20 = sum(prices[-20:]) / 20
            ma50 = sum(prices[-50:]) / 50

            if ma20 > ma50:
                return "BUY"

            elif ma20 < ma50:
                return "SELL"

            return "WAIT"

        m5 = trend(m5_prices)
        m15 = trend(m15_prices)
        h1 = trend(h1_prices)

        buy = 0
        sell = 0

        for signal in (m5, m15, h1):

            if signal == "BUY":
                buy += 1

            elif signal == "SELL":
                sell += 1

        if buy == 3:
            return "STRONG_MULTI_BUY", 30

        elif sell == 3:
            return "STRONG_MULTI_SELL", 30

        elif buy == 2:
            return "MULTI_BUY", 15

        elif sell == 2:
            return "MULTI_SELL", 15

        return "NO_CONFIRMATION", 0