class RiskManager:

    def __init__(self, risk_percent=1.0):
        self.risk_percent = risk_percent

    def calculate_lot_size(self, balance, stop_loss_pips, pip_value=10):
        """
        balance: Account balance
        stop_loss_pips: Stop loss distance in pips
        pip_value: Value of 1 pip for 1.00 lot (approximate)
        """

        if stop_loss_pips <= 0:
            return 0.0

        risk_amount = balance * (self.risk_percent / 100)

        lot_size = risk_amount / (stop_loss_pips * pip_value)

        return round(lot_size, 2)