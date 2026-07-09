from market_scanner import MarketScanner
from performance_analyzer import PerformanceAnalyzer


class BotEngine:

    def __init__(self):
        self.scanner = MarketScanner()
        self.performance = PerformanceAnalyzer()

    def run(self, markets):

        results = []

        for symbol, market_data in markets.items():

            result = self.scanner.scan(
                symbol,
                market_data
            )

            self.performance.update(
                result["decision"]
            )

            results.append(result)

        results.sort(
            key=lambda trade: trade["score"],
            reverse=True
        )

        return results

    def report(self):
        self.performance.report()