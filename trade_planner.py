class TradePlanner:

    def plan_buy(self, entry, atr):

        stop_loss = entry - (atr * 2)

        take_profit = entry + (atr * 4)

        return {
            "entry": round(entry, 5),
            "stop_loss": round(stop_loss, 5),
            "take_profit": round(take_profit, 5),
            "risk_reward": "1:2"
        }

    def plan_sell(self, entry, atr):

        stop_loss = entry + (atr * 2)

        take_profit = entry - (atr * 4)

        return {
            "entry": round(entry, 5),
            "stop_loss": round(stop_loss, 5),
            "take_profit": round(take_profit, 5),
            "risk_reward": "1:2"
        }