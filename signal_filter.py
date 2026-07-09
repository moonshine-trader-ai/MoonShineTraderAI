class SignalFilter:

    def filter(
        self,
        decision,
        confidence,
        spread_ok=True
    ):

        if decision == "WAIT":
            return False

        if confidence < 70:
            return False

        if not spread_ok:
            return False

        return True