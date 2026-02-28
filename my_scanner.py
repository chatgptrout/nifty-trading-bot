import streamlit as st
import yfinance as yf
import pandas as pd

# Streamlit UI
st.title("📈 Nifty Live Tracker")

def check_market():
    ticker = "^NSEI"
    data = yf.download(tickers=ticker, period='1d', interval='1m', progress=False)
    
    if not data.empty:
        current_price = float(data['Close'].iloc[-1])
        avg_5min = float(data['Close'].tail(5).mean())
        
        st.metric("Nifty Price", f"₹{current_price:.2f}")
        
        if current_price > avg_5min:
            st.success("🚀 SIGNAL: Trend is UP (Bullish)")
        else:
            st.error("📉 SIGNAL: Trend is DOWN (Bearish)")
        
        st.line_chart(data['Close'])
    else:
        st.write("Data fetching mein dikkat hai.")

# Button click par refresh hoga
if st.button('Refresh Price'):
    check_market()
else:
    check_market()
