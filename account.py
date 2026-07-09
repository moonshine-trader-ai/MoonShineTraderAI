import MetaTrader5 as mt5


class TradingAccount:

    def __init__(self):

        info = mt5.account_info()

        if info is None:
            raise Exception(
                f"Unable to read MT5 account: {mt5.last_error()}"
            )

        self.balance = float(info.balance)
        self.equity = float(info.equity)

        positions = mt5.positions_get()

        if positions is None:
            self.open_trades = 0
        else:
            self.open_trades = len(positions)

        self.daily_loss = max(
            0.0,
            self.balance - self.equity
        )

    def show(self):

        print("========== ACCOUNT ==========")
        print("Balance      :", self.balance)
        print("Equity       :", self.equity)
        print("Open Trades  :", self.open_trades)
        print("Daily Loss   :", round(self.daily_loss, 2))
        print("=============================")