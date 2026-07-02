class Backtester:

    def __init__(self):
        self.total_trades = 0
        self.wins = 0
        self.losses = 0
        self.net_profit = 0.0

    def record_trade(self, profit):

        self.total_trades += 1

        if profit > 0:
            self.wins += 1
        else:
            self.losses += 1

        self.net_profit += profit

    def report(self):

        print("\n========== BACKTEST REPORT ==========")

        print("Total Trades :", self.total_trades)
        print("Winning Trades :", self.wins)
        print("Losing Trades :", self.losses)

        if self.total_trades > 0:
            win_rate = (self.wins / self.total_trades) * 100
        else:
            win_rate = 0

        print("Win Rate :", round(win_rate, 2), "%")
        print("Net Profit :", round(self.net_profit, 2))

        print("=====================================")