from trend_analyzer import TrendAnalyzer
from momentum_analyzer import MomentumAnalyzer
from ema_analyzer import EMAAnalyzer
from macd_analyzer import MACDAnalyzer
from atr_analyzer import ATRAnalyzer


class IndicatorManager:

    def analyze(
        self,
        prices,
        rates
    ):

        current_price = prices[-1]

        ma5 = sum(prices[-5:]) / 5
        ma10 = sum(prices[-10:]) / 10

        # RSI
        gains = []
        losses = []

        for i in range(1, 15):

            change = prices[-15 + i] - prices[-16 + i]

            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))

        average_gain = sum(gains) / 14
        average_loss = sum(losses) / 14

        if average_loss == 0:
            rsi = 100
        else:
            rs = average_gain / average_loss
            rsi = 100 - (100 / (1 + rs))

        trend = TrendAnalyzer()
        momentum = MomentumAnalyzer()
        ema = EMAAnalyzer()
        macd = MACDAnalyzer()
        atr = ATRAnalyzer()

        trend_name, trend_score = trend.analyze(
            current_price,
            ma5,
            ma10
        )

        momentum_name, momentum_score = momentum.analyze(rsi)

        ema_name, ema_score, ema20, ema50, ema200 = ema.analyze(prices)

        macd_name, macd_score, macd_value = macd.analyze(prices)

        atr_value = atr.calculate(rates)

        return {
            "trend_name": trend_name,
            "trend_score": trend_score,
            "momentum_name": momentum_name,
            "momentum_score": momentum_score,
            "ema_name": ema_name,
            "ema_score": ema_score,
            "ema20": ema20,
            "ema50": ema50,
            "ema200": ema200,
            "macd_name": macd_name,
            "macd_score": macd_score,
            "macd_value": macd_value,
            "atr": atr_value
        }