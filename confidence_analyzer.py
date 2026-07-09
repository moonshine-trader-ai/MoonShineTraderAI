class ConfidenceAnalyzer:

    def calculate(self, buy_score, sell_score):

        total = buy_score + sell_score

        if total == 0:
            return 0

        confidence = (max(buy_score, sell_score) / total) * 100

        return round(confidence, 1)