class Indicators:

    def calculate_ema(self, prices, period):

        if len(prices) < period:
            return None

        multiplier = 2 / (period + 1)

        ema = sum(prices[:period]) / period

        for price in prices[period:]:
            ema = (price - ema) * multiplier + ema

        return round(ema, 5)

    def calculate_rsi(self, prices, period=14):

        if len(prices) <= period:
            return None

        gains = []
        losses = []

        for i in range(1, len(prices)):
            change = prices[i] - prices[i - 1]

            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))

        average_gain = sum(gains[:period]) / period
        average_loss = sum(losses[:period]) / period

        for i in range(period, len(gains)):
            average_gain = ((average_gain * (period - 1)) + gains[i]) / period
            average_loss = ((average_loss * (period - 1)) + losses[i]) / period

        if average_loss == 0:
            return 100.0

        rs = average_gain / average_loss
        rsi = 100 - (100 / (1 + rs))

        return round(rsi, 2)