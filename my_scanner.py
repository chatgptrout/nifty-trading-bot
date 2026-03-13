import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Breakout with Target/SL", layout="wide")
st.title("🚀 Breakout Scanner: Target & SL")

stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'INFY.NS', 'BHARTIARTL.NS', 'SBIN.NS', 'ITC.NS', 'ADANIENT.NS', 'TATAMOTORS.NS']

def scan_with_levels():
    results = []
    for symbol in stocks:
        data = yf.download(symbol, period='2d', interval='5m', progress=False)
        if len(data) >= 2:
            current_price = float(data['Close'].iloc[-1])
            prev_high = float(data['High'].iloc[:-1].max())
            prev_low = float(data['Low'].iloc[:-1].min())
            
            # Simple Intraday Logic:
            # Target = Buy Price + 1% | SL = Buy Price - 0.5%
            target = prev_high * 1.01
            sl = prev_high * 0.995
            
            status = "🚀 BREAKOUT" if current_price > prev_high else "📉 BREAKDOWN" if current_price < prev_low else "⚖️ WAIT"
            
            results.append({
                "Stock": symbol.replace(".NS", ""),
                "Price": current_price,
                "Buy Above": prev_high,
                "Target (1%)": round(target, 2),
                "Stop Loss": round(sl, 2),
                "Status": status
            })

    df = pd.DataFrame(results)
    st.table(df)

if st.button('Scan Market'):
    scan_with_levels()
else:
    scan_with_levels()
