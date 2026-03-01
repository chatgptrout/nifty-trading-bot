import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Nifty Levels Bot", layout="wide")
st.title("📈 Nifty Live Levels & Signals")

def get_levels_and_signals():
    ticker = "^NSEI"
    # Data fetch karna
    data = yf.download(tickers=ticker, period='2d', interval='1m', progress=False)
    
    if not data.empty:
        current_price = float(data['Close'].iloc[-1])
        
        # Friday (Previous Day) ke Levels
        # Hum pichle din ka data nikal rahe hain
        history = yf.Ticker(ticker).history(period="2d")
        friday_high = float(history['High'].iloc[0])
        friday_low = float(history['Low'].iloc[0])
        
        # Display Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Live Price", f"₹{current_price:.2f}")
        col2.metric("Buy Above (High)", f"₹{friday_high:.2f}")
        col3.metric("Sell Below (Low)", f"₹{friday_low:.2f}")

        # Signal Logic
        st.subheader("📢 Trading Signal")
        if current_price > friday_high:
            st.success(f"🚀 BULLISH: Buy Above {friday_high:.2f}")
        elif current_price < friday_low:
            st.error(f"📉 BEARISH: Sell Below {friday_low:.2f}")
        else:
            st.info("⚖️ SIDEWAYS: No Trade Zone (Waiting for Breakout)")

        # Chart
        st.line_chart(data['Close'])
    else:
        st.error("Market data load nahi ho raha.")

get_levels_and_signals()

if st.button('Refresh Page'):
    st.rerun()
