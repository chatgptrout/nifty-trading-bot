import streamlit as st
import yfinance as yf

st.title("📈 Nifty Live Tracker")

# Sirf ek baar data check karne ka function
def check_price():
    data = yf.download("^NSEI", period='1d', interval='1m', progress=False)
    if not data.empty:
        price = float(data['Close'].iloc[-1])
        st.metric("Nifty Price", f"₹{price:.2f}")
        st.line_chart(data['Close'])
    else:
        st.error("Data nahi mil raha.")

check_price()

if st.button('Refresh'):
    st.rerun()
