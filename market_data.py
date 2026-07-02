# Simulated market data

prices = [
    1.1010, 1.1015, 1.1020, 1.1025, 1.1030,
    1.1035, 1.1040, 1.1045, 1.1050, 1.1055,
    1.1060, 1.1065, 1.1070, 1.1075, 1.1080,
    1.1085, 1.1090, 1.1095, 1.1100, 1.1105
]

def get_prices():
    return prices

def get_current_price():
    return prices[-1]