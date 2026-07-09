from datetime import datetime


class SessionAnalyzer:

    def analyze(self):

        hour = datetime.now().hour

        # London + New York overlap
        if 13 <= hour < 17:
            return "LONDON_NEWYORK_OVERLAP", 15

        # London session
        elif 8 <= hour < 13:
            return "LONDON_SESSION", 10

        # New York session
        elif 17 <= hour < 22:
            return "NEW_YORK_SESSION", 10

        # Asian / quiet market
        else:
            return "LOW_LIQUIDITY", 0