import asyncio, os, time, traceback
from token_fetcher import fetch_tokens
from config import should_trade_token, execute_trade, log_profit

AUD_CAP = 10000
AUD_MIN_GOAL = 3000
PROFIT_LOG = 'profit_log.csv'

wallet = {'sol_balance': 0.5, 'aud_profit': 0.0}  # start example

def aud_to_sol(aud):
    return aud / 250  # placeholder rate

def sol_to_aud(sol):
    return sol * 250

async def trade_token(token):
    try:
        if not should_trade_token(token):
            return
        result = await execute_trade(token, wallet)
        if result:
            log_profit(token, result['profit'], PROFIT_LOG)
            wallet['aud_profit'] += result['profit']
    except Exception as e:
        print("[ERROR]", e)
        traceback.print_exc()
        # Future: auto-send traceback to ChatGPT

async def run():
    while wallet['aud_profit'] < AUD_CAP:
        tokens = fetch_tokens()
        await asyncio.gather(*(trade_token(t) for t in tokens))
        await asyncio.sleep(5)

    print("[INFO] Daily profit cap reached. Stopping.")

def run_trading_bot():
    asyncio.run(run())
