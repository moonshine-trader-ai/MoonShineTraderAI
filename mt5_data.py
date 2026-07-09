import MetaTrader5 as mt5


class MT5Data:

    def __init__(self):

        if not mt5.initialize():
            raise Exception(
                f"MT5 initialization failed: {mt5.last_error()}"
            )

    def get_rates(
        self,
        symbol,
        timeframe=mt5.TIMEFRAME_M5,
        candles=100
    ):

        if not mt5.symbol_select(symbol, True):
            return []

        rates = mt5.copy_rates_from_pos(
            symbol,
            timeframe,
            0,
            candles
        )

        if rates is None or len(rates) == 0:
            return []

        return rates

    def get_close_prices(
        self,
        symbol,
        timeframe=mt5.TIMEFRAME_M5,
        candles=100
    ):

        rates = self.get_rates(
            symbol,
            timeframe,
            candles
        )

        return [float(candle["close"]) for candle in rates]

    def get_spread(self, symbol):

        tick = mt5.symbol_info_tick(symbol)

        if tick is None:
            return None

        return abs(tick.ask - tick.bid)

    def shutdown(self):

        mt5.shutdown()