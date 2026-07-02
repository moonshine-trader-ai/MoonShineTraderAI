class DecisionEngine:

    def __init__(self):
        self.score = 0
        self.reasons = []

    def add_score(self, points, reason):
        self.score += points
        self.reasons.append(f"+{points} : {reason}")

    def calculate(self):

        if self.score >= 90:
            return "STRONG BUY"

        elif self.score >= 80:
            return "BUY"

        elif self.score >= 60:
            return "WAIT"

        elif self.score >= 40:
            return "WEAK SELL"

        else:
            return "SELL"

    def report(self):
        return self.calculate(), self.score, self.reasons