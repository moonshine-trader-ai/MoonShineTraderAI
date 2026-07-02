from datetime import datetime

class SessionAnalyzer:

    def analyze(self):

        hour = datetime.now().hour

        if 8 <= hour < 17:
            return "LONDON_SESSION", 10

        elif 13 <= hour < 22:
            return "NEW_YORK_SESSION", 10

        elif 8 <= hour < 22:
            return "LONDON_NEWYORK_OVERLAP", 15

        else:
            return "LOW_LIQUIDITY", 0