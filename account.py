class TradingAccount:

    def __init__(self):
        self.balance = 10000.00
        self.equity = 10000.00
        self.open_trades = 0
        self.daily_loss = 0.0

    def show(self):
        print("========== ACCOUNT ==========")
        print("Balance      :", self.balance)
        print("Equity       :", self.equity)
        print("Open Trades  :", self.open_trades)
        print("Daily Loss   :", self.daily_loss)
        print("=============================")