from datetime import datetime
import os


class TradeJournal:

    def __init__(self):

        self.filename = "trade_journal.txt"

    def save(self, symbol, decision, score, reasons):

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        lines = [
            "\n========== TRADE JOURNAL ==========",
            f"Time : {now}",
            f"Pair : {symbol}",
            f"Decision : {decision}",
            f"Score : {score}",
            "",
            "Reasons:"
        ]

        for reason in reasons:
            lines.append(f"- {reason}")

        lines.append("===================================")

        # Print to terminal
        for line in lines:
            print(line)

        # Save to file
        with open(self.filename, "a", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")