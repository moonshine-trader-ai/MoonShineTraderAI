import logger

def execute_trade(signal, score):
    if signal == "BUY":
        logger.log(f"BUY order prepared (Confidence: {score}%)")

    elif signal == "SELL":
        logger.log(f"SELL order prepared (Confidence: {score}%)")

    else:
        logger.log("No trade executed. Waiting for a better setup.")