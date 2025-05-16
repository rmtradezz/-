# Solana Meme Coin Trading Bot 🤖💰

This is a real-money Solana trading bot built to automatically:
- Detect and buy trending meme coins (especially 1K–100K market cap)
- Apply rugpull filters via [rugcheck.xyz](https://rugcheck.xyz)
- Follow social signals from influencers on X.com (Elon Musk, Trump, etc.)
- Execute real Raydium trades with dynamic sizing and stop-loss
- Maximize profits 24/7 with smart daily/weekly targets

---

## 🔧 Features

- ✅ ~$50 buys for fresh low caps
- ✅ High-conviction buys for safe tokens
- ✅ 20% stop-loss to avoid big losses
- ✅ Profit tracking in AUD with CSV logs
- ✅ Parallel trading via asyncio
- ✅ ChatGPT fallback for automated issue diagnosis
- ✅ Full deployment on Render.com

---

## 📦 Files

- `main.py`: Starts the trading loop
- `trade_engine.py`: Core bot logic
- `token_fetcher.py`: Trending token + safety filter
- `config.py`: Trade rules, filters, and simulation
- `requirements.txt`: Python packages
- `start.sh`: Shell script for Render
- `render.yaml`: Render deployment setup
- `profit_log.csv`: Profit history
- `README.md`: You’re reading it 👀

---

## 🚀 How to Deploy on [Render](https://render.com)

1. **Upload everything to a GitHub repo**
2. **Go to Render → New Web Service**
3. **Connect your repo**
4. Render auto-detects `render.yaml`
5. Add env var:  
   `PRIVATE_KEY = your_solana_private_key`
6. Click **Deploy**

---

## ⚠️ Important

- **Use a burner wallet**
- **Don’t invest more than you can lose**
- This bot is aggressive but **includes stop-loss & smart filters**
- Fully async and designed for 24/7 profit extraction

---

## 👀 Coming Next

- ✅ Real Raydium swap integration
- ✅ Influencer-based token filtering from X.com
- ✅ Crash detection + auto-healing via GPT
- ⏳ Telegram/Discord alerts (coming soon)

---

Made for educational and high-performance trading experimentation 🧪

