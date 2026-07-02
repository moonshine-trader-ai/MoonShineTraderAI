class PerformanceAnalyzer:

    def __init__(self):

        self.total_scans = 0
        self.buy = 0
        self.sell = 0
        self.wait = 0

    def update(self, decision):

        self.total_scans += 1

        if "BUY" in decision:
            self.buy += 1

        elif "SELL" in decision:
            self.sell += 1

        else:
            self.wait += 1

    def report(self):

        print("\n========== PERFORMANCE ==========")

        print("Total Scans :", self.total_scans)
        print("BUY Signals :", self.buy)
        print("SELL Signals:", self.sell)
        print("WAIT Signals:", self.wait)

        print("=================================\n")