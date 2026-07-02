def analyze_market(price, ema50, ema200, rsi):
    score = 0

    if price > ema50:
        score += 30

    if ema50 > ema200:
        score += 30

    if rsi > 55:
        score += 40

    if score >= 80:
        return "BUY", score

    elif price < ema50 and ema50 < ema200 and rsi < 45:
        return "SELL", 100

    else:
        return "WAIT", score