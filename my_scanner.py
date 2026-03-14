import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime
import pytz

st.set_page_config(page_title="Pro Breakout Scanner", layout="wide")

# India Timezone
IST = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(IST).strftime('%Y-%m-%d | %H:%M:%S')

st.title("🚀 Intraday Breakout Scanner")
st.subheader(f"🕒 Time: {current_time} (IST)")

stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'INFY.NS', 'BHARTIARTL.NS', 'SBIN.NS', 'ITC.NS', 'ADANIENT.NS', 'TATAMOTORS.NS']

def scan_market():
    results = []
    for symbol in stocks:
        data = yf.download(symbol, period='2d', interval='5m', progress=False)
        if len(data) >= 2:
            current_price = float(data['Close'].iloc[-1])
            prev_high = float(data['High'].iloc[:-1].max())
            prev_low = float(data['Low'].iloc[:-1].min())
            volume = int(data['Volume'].iloc[-1]) # Current Volume
            
            # Target (1%) & SL (0.5%)
            target = prev_high * 1.01
            sl = prev_high * 0.995
            
            status = "🚀 BREAKOUT" if current_price > prev_high else "📉 BREAKDOWN" if current_price < prev_low else "⚖️ WAIT"
            
            results.append({
                "Stock": symbol.replace(".NS", ""),
                "Price": round(current_price, 2),
                "Buy Above": round(prev_high, 2),
                "Target": round(target, 2),
                "Stop Loss": round(sl, 2),
                "Volume": volume,
                "Status": status
            })

    st.table(pd.DataFrame(results))

if st.button('🔄 Refresh Market Data'):
    scan_market()
else:
    scan_market()
    
