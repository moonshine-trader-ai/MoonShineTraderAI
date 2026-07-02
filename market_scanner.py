from trend_analyzer import TrendAnalyzer
from candlestick_analyzer import CandlestickAnalyzer
from support_resistance import SupportResistanceAnalyzer
from momentum_analyzer import MomentumAnalyzer
from spread_analyzer import SpreadAnalyzer
from decision_engine import DecisionEngine
from trade_journal import TradeJournal

class MarketScanner:

    def scan(self, symbol, prices):

        current_price = prices[-1]

        ma5 = sum(prices[-5:]) / 5
        ma10 = sum(prices[-10:]) / 10

        rsi = 62

        # Temporary spread values
        spreads = {
            "EURUSD": 1.2,
            "GBPUSD": 2.1,
            "USDJPY": 1.5,
            "XAUUSD": 25
        }

        spread = spreads[symbol]

        trend = TrendAnalyzer()
        candle = CandlestickAnalyzer()
        sr = SupportResistanceAnalyzer()
        momentum = MomentumAnalyzer()
        spread_checker = SpreadAnalyzer()
        journal = TradeJournal()

        trend_name, trend_score = trend.analyze(current_price, ma5, ma10)

        pattern_name, pattern_score = candle.analyze(
            prices[-2],
            current_price + 0.0003,
            current_price - 0.0003,
            current_price
        )

        support, resistance, sr_score, sr_reason = sr.analyze(
            current_price,
            prices
        )

        momentum_name, momentum_score = momentum.analyze(rsi)

        spread_name, spread_score = spread_checker.analyze(
            symbol,
            spread
        )

        engine = DecisionEngine()

        engine.add_score(trend_score, trend_name)
        engine.add_score(pattern_score, pattern_name)
        engine.add_score(sr_score, sr_reason)
        engine.add_score(momentum_score, momentum_name)
        engine.add_score(spread_score, spread_name)
        engine.add_score(10, "SESSION_OK")
        engine.add_score(10, "RISK_OK")

        decision, score, reasons = engine.report()

        journal.save(symbol, decision, score, reasons)

        return {
            "symbol": symbol,
            "decision": decision,
            "score": score,
            "reasons": reasons
        }