from datetime import datetime

class TradeJournal:

    def save(self, symbol, decision, score, reasons):

        print("\n========== TRADE JOURNAL ==========")
        print("Time :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Pair :", symbol)
        print("Decision :", decision)
        print("Score :", score)

        print("\nReasons:")

        for reason in reasons:
            print("-", reason)

        print("===================================\n")