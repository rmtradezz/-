import random

def should_trade_token(token):
    mc = token.get('market_cap', 0)
    return 1000 <= mc <= 1000000

def execute_trade(token, wallet):
    symbol = token['symbol']
    if token['market_cap'] < 100000:
        amount_aud = 50
    else:
        amount_aud = min(500, sol_to_aud(wallet['sol_balance'] / 4))

    stop_loss = amount_aud * 0.8
    profit = random.uniform(0.05, 0.5) * amount_aud
    print(f"[TRADE] {symbol}: Buy {amount_aud} AUD | Profit {profit:.2f} AUD")
    return {'profit': profit}

def sol_to_aud(sol):
    return sol * 250

def log_profit(symbol, profit, filename):
    with open(filename, 'a') as f:
        f.write(f"{symbol},{profit}\n")
