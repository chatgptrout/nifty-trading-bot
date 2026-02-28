import streamlit as st
import yfinance as yf
import pandas as pd

# Dashboard ka Title
st.set_page_config(page_title="Nifty Live Bot", layout="wide")
st.title("📈 Nifty 50 Live Trading Bot")

def get_market_data():
    ticker = "^NSEI"
    # Yahoo Finance se data lena
    data = yf.download(tickers=ticker, period='1d', interval='1m', progress=False)
    
    if not data.empty:
        # Latest price aur average nikalna
        current_price = float(data['Close'].iloc[-1])
        avg_5min = float(data['Close'].tail(5).mean())
        
        # Badi metrics dikhana
        st.metric(label="Current Nifty Price", value=f"₹{current_price:.2f}")
        
        # Signal dikhana
        if current_price > avg_5min:
            st.success("🚀 SIGNAL: Trend is UP (Bullish)")
        else:
            st.error("📉 SIGNAL: Trend is DOWN (Bearish)")
            
        # Chart dikhana
        st.line_chart(data['Close'])
    else:
        st.warning("Market data abhi available nahi hai. Kal subah 9:15 par check karein.")

# Loop hatakar seedha function call karna
get_market_data()

# Refresh button taaki user manually update kar sake
if st.button('Update Live Price'):
    st.rerun()
