class PerformanceAnalyzer:

    def __init__(self):
        self.total = 0
        self.buy = 0
        self.sell = 0
        self.wait = 0

    def update(self, decision):
        self.total += 1

        if decision == "BUY":
            self.buy += 1

        elif decision == "SELL":
            self.sell += 1

        else:
            self.wait += 1

    def report(self):
        print("\n========== PERFORMANCE ==========")
        print(f"Total Scans : {self.total}")
        print(f"BUY Signals : {self.buy}")
        print(f"SELL Signals: {self.sell}")
        print(f"WAIT Signals: {self.wait}")
        print("=================================\n")