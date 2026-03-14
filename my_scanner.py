import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime
import pytz

# Page Configuration
st.set_page_config(page_title="Pro Trading Scanner", layout="wide")

# 🕒 Live Clock
IST = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(IST).strftime('%d-%m-%Y | %H:%M:%S')

st.title("🚀 Live Breakout & OI Scanner")
st.subheader(f"🕒 Time: {current_time} (IST)")

# Watchlist
stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'INFY.NS', 'SBIN.NS', 'ITC.NS', 'ADANIENT.NS']

def get_market_data():
    results = []
    for s in stocks:
        # Data fetch from Yahoo Finance (Stable)
        data = yf.download(s, period='2d', interval='5m', progress=False)
        if not data.empty:
            lp = float(data['Close'].iloc[-1])
            ph = float(data['High'].iloc[:-1].max())
            
            # Target (1%) aur SL (0.5%)
            target = ph * 1.01
            sl = ph * 0.995
            
            # Status Logic
            status = "🚀 BREAKOUT" if lp > ph else "⚖️ WAIT"
            
            results.append({
                "Stock": s.replace(".NS", ""),
                "Price": round(lp, 2),
                "Buy Above": round(ph, 2),
                "Target": round(target, 2),
                "Stop Loss": round(sl, 2),
                "OI (Open Interest)": "48.2L", # Asli OI ke liye API fix bad mein karenge
                "Status": status
            })
    return pd.DataFrame(results)

# Display Table
df = get_market_data()
st.table(df)

if st.button('🔄 Manual Refresh'):
    st.rerun()
