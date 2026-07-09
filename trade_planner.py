class TradePlanner:

    def plan(
        self,
        decision,
        current_price,
        atr,
        risk_reward=2.0
    ):

        if atr <= 0:

            return {
                "entry": current_price,
                "stop_loss": current_price,
                "take_profit": current_price
            }

        if "BUY" in decision:

            stop_loss = current_price - (atr * 2)
            take_profit = current_price + ((atr * 2) * risk_reward)

        elif "SELL" in decision:

            stop_loss = current_price + (atr * 2)
            take_profit = current_price - ((atr * 2) * risk_reward)

        else:

            stop_loss = current_price
            take_profit = current_price

        return {
            "entry": round(current_price, 5),
            "stop_loss": round(stop_loss, 5),
            "take_profit": round(take_profit, 5)
        }