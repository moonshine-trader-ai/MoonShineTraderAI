from backtester import Backtester

backtester = Backtester()

# Sample trade results (profits and losses)
sample_results = [
    120,
    -50,
    80,
    200,
    -100,
    150,
    -30,
    90,
    60,
    -40
]

for result in sample_results:
    backtester.record_trade(result)

backtester.report()