import streamlit as st
import yfinance as yf
import pandas as pd

# Dashboard Title
st.title("📈 Nifty Live Trading Bot")

# Data Fetching Function
def get_signals():
    ticker = "^NSEI"
    data = yf.download(tickers=ticker, period='1d', interval='1m', progress=False)
    
    if not data.empty:
        current_price = float(data['Close'].iloc[-1])
        avg_5min = float(data['Close'].tail(5).mean())
        
        # Metrics display
        st.metric("Nifty 50 Live Price", f"₹{current_price:.2f}")
        
        if current_price > avg_5min:
            st.success("🚀 SIGNAL: Trend is UP (Bullish)")
        else:
            st.error("📉 SIGNAL: Trend is DOWN (Bearish)")
            
        # Chart display
        st.line_chart(data['Close'])
    else:
        st.error("Data fetch nahi ho raha. Market hours check karein.")

# Auto-run function
get_signals()

# Manual Refresh Button
if st.button('Update Live Price'):
    st.rerun()
