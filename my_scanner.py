import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Trading Bot: Nifty & MCX", layout="wide")
st.title("📊 Live Trading Dashboard: Nifty | Crude | NG")

def get_data(ticker, name):
    data = yf.download(tickers=ticker, period='2d', interval='1m', progress=False)
    if not data.empty:
        current_price = float(data['Close'].iloc[-1])
        history = yf.Ticker(ticker).history(period="2d")
        prev_high = float(history['High'].iloc[0])
        prev_low = float(history['Low'].iloc[0])
        
        st.subheader(f"💎 {name}")
        c1, c2, c3 = st.columns(3)
        c1.metric("Live Price", f"₹{current_price:.2f}")
        c2.metric("Buy Above", f"₹{prev_high:.2f}")
        c3.metric("Sell Below", f"₹{prev_low:.2f}")
        
        if current_price > prev_high:
            st.success(f"🚀 {name}: BULLISH Signal")
        elif current_price < prev_low:
            st.error(f"📉 {name}: BEARISH Signal")
        else:
            st.info(f"⚖️ {name}: Sideways Zone")
        st.divider()

# Symbols for Nifty, Crude Oil, and Natural Gas
# Note: MCX symbols yfinance mein 'CL=F' (Crude) aur 'NG=F' (Natural Gas) hote hain
get_data("^NSEI", "NIFTY 50")
get_data("CL=F", "CRUDE OIL (Global)")
get_data("NG=F", "NATURAL GAS (Global)")

if st.button('Refresh All Data'):
    st.rerun()
