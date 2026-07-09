class DecisionEngine:

    def __init__(self):
        self.buy_score = 0
        self.sell_score = 0
        self.reasons = []

    def add_buy(self, points, reason):
        self.buy_score += points
        self.reasons.append(f"BUY +{points} : {reason}")

    def add_sell(self, points, reason):
        self.sell_score += points
        self.reasons.append(f"SELL +{points} : {reason}")

    def report(self):

        if self.buy_score >= self.sell_score + 20:

            if self.buy_score >= 90:
                decision = "STRONG BUY"
            elif self.buy_score >= 70:
                decision = "BUY"
            else:
                decision = "WAIT"

        elif self.sell_score >= self.buy_score + 20:

            if self.sell_score >= 90:
                decision = "STRONG SELL"
            elif self.sell_score >= 70:
                decision = "SELL"
            else:
                decision = "WAIT"

        else:
            decision = "WAIT"

        return decision, self.buy_score, self.sell_score, self.reasons