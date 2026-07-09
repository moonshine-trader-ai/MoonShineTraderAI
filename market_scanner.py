from indicator_manager import IndicatorManager
from multi_timeframe import MultiTimeframeAnalyzer
from candlestick_analyzer import CandlestickAnalyzer
from support_resistance import SupportResistanceAnalyzer
from spread_analyzer import SpreadAnalyzer
from session_analyzer import SessionAnalyzer
from trade_planner import TradePlanner
from confidence_analyzer import ConfidenceAnalyzer
from signal_filter import SignalFilter
from decision_engine import DecisionEngine
from trade_journal import TradeJournal


class MarketScanner:

    def scan(self, symbol, market_data):

        rates = market_data["rates"]
        prices = market_data["prices"]
        spread = market_data["spread"]

        m5_prices = market_data["m5_prices"]
        m15_prices = market_data["m15_prices"]
        h1_prices = market_data["h1_prices"]

        current_price = prices[-1]

        indicators = IndicatorManager()

        result = indicators.analyze(
            prices,
            rates
        )

        trend_name = result["trend_name"]
        trend_score = result["trend_score"]

        momentum_name = result["momentum_name"]
        momentum_score = result["momentum_score"]

        ema_name = result["ema_name"]
        ema_score = result["ema_score"]

        macd_name = result["macd_name"]
        macd_score = result["macd_score"]

        atr = result["atr"]

        mtf = MultiTimeframeAnalyzer()

        mtf_name, mtf_score = mtf.analyze(
            m5_prices,
            m15_prices,
            h1_prices
        )

        last = rates[-1]

        open_price = float(last["open"])
        high = float(last["high"])
        low = float(last["low"])
        close = float(last["close"])

        candle = CandlestickAnalyzer()

        pattern_name, pattern_score = candle.analyze(
            open_price,
            high,
            low,
            close
        )

        sr = SupportResistanceAnalyzer()

        support, resistance, sr_score, sr_reason = sr.analyze(
            symbol,
            current_price,
            prices
        )

        spread_checker = SpreadAnalyzer()

        spread_name, spread_score = spread_checker.analyze(
            symbol,
            spread
        )

        session = SessionAnalyzer()

        session_name, session_score = session.analyze()

        planner = TradePlanner()
        confidence = ConfidenceAnalyzer()
        filter_engine = SignalFilter()

        engine = DecisionEngine()
                trend_is_buy = False

        # Trend
        if "UPTREND" in trend_name:
            engine.add_buy(trend_score, trend_name)
            trend_is_buy = True

        elif "DOWNTREND" in trend_name:
            engine.add_sell(trend_score, trend_name)

        # Multi-Timeframe Confirmation
        if "STRONG_MULTI_BUY" == mtf_name:
            engine.add_buy(mtf_score, mtf_name)

        elif "STRONG_MULTI_SELL" == mtf_name:
            engine.add_sell(mtf_score, mtf_name)

        elif "MULTI_BUY" == mtf_name:
            engine.add_buy(mtf_score, mtf_name)

        elif "MULTI_SELL" == mtf_name:
            engine.add_sell(mtf_score, mtf_name)

        # EMA
        if "BULLISH" in ema_name:
            engine.add_buy(ema_score, ema_name)

        elif "BEARISH" in ema_name:
            engine.add_sell(ema_score, ema_name)

        # MACD
        if "BULLISH" in macd_name:
            engine.add_buy(macd_score, macd_name)

        elif "BEARISH" in macd_name:
            engine.add_sell(macd_score, macd_name)

        # Momentum
        if momentum_name in (
            "GOOD_MOMENTUM",
            "STRONG_MOMENTUM"
        ):
            engine.add_buy(momentum_score, momentum_name)

        elif momentum_name in (
            "WEAK_MOMENTUM",
            "BEARISH_MOMENTUM",
            "GOOD_BEARISH_MOMENTUM",
            "STRONG_BEARISH_MOMENTUM"
        ):
            engine.add_sell(momentum_score, momentum_name)

        # Candlestick
        if pattern_name in (
            "BULLISH_ENGULFING",
            "HAMMER"
        ):
            engine.add_buy(pattern_score, pattern_name)

        elif pattern_name in (
            "BEARISH_ENGULFING",
            "SHOOTING_STAR"
        ):
            engine.add_sell(pattern_score, pattern_name)

        # Support / Resistance
        if "SUPPORT" in sr_reason:
            engine.add_buy(sr_score, sr_reason)

        elif "RESISTANCE" in sr_reason:
            engine.add_sell(sr_score, sr_reason)

        # Spread
        if spread_name == "SPREAD_OK":

            if trend_is_buy:
                engine.add_buy(spread_score, spread_name)
            else:
                engine.add_sell(spread_score, spread_name)

        # Session
        if session_score > 0:

            if trend_is_buy:
                engine.add_buy(session_score, session_name)
            else:
                engine.add_sell(session_score, session_name)

        # Risk
        if trend_is_buy:
            engine.add_buy(10, "RISK_OK")
        else:
            engine.add_sell(10, "RISK_OK")

        decision, buy_score, sell_score, reasons = engine.report()

        confidence_score = confidence.calculate(
            buy_score,
            sell_score
        )

        trade_allowed = filter_engine.filter(
            decision,
            confidence_score,
            spread_name == "SPREAD_OK"
        )

        plan = planner.plan(
            decision,
            current_price,
            atr
        )

        journal = TradeJournal()

        journal.save(
            symbol,
            decision,
            max(buy_score, sell_score),
            reasons
        )

        return {
            "symbol": symbol,
            "decision": decision,
            "score": max(buy_score, sell_score),
            "buy_score": buy_score,
            "sell_score": sell_score,
            "confidence": confidence_score,
            "trade_allowed": trade_allowed,
            "entry": plan["entry"],
            "stop_loss": plan["stop_loss"],
            "take_profit": plan["take_profit"],
            "atr": atr,
            "reasons": reasons
        }