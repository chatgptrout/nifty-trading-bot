import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stock Breakout Scanner", layout="wide")
st.title("🚀 Intraday Breakout & Breakdown Scanner")
st.write("Ye scanner Nifty ke top stocks ko scan karke breakout levels batata hai.")

# Stocks ki list (Aap yahan aur bhi stocks add kar sakte hain)
stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'INFY.NS', 'BHARTIARTL.NS', 'SBIN.NS', 'ITC.NS', 'ADANIENT.NS', 'TATAMOTORS.NS']

def scan_stocks():
    breakout_list = []
    breakdown_list = []
    watchdown_list = []

    for symbol in stocks:
        data = yf.download(symbol, period='2d', interval='5m', progress=False)
        if not data.empty:
            current_price = data['Close'].iloc[-1]
            prev_high = data['High'].iloc[:-1].max() # Kal ka High
            prev_low = data['Low'].iloc[:-1].min()   # Kal ka Low
            
            # Logic for Breakout/Breakdown
            if current_price > prev_high:
                breakout_list.append([symbol, current_price, prev_high, "🚀 BREAKOUT"])
            elif current_price < prev_low:
                breakdown_list.append([symbol, current_price, prev_low, "📉 BREAKDOWN"])
            else:
                watchdown_list.append([symbol, current_price, prev_high, prev_low])

    # Display Results
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("🔥 Breakout Stocks")
        if breakout_list:
            df_up = pd.DataFrame(breakout_list, columns=['Stock', 'Price', 'High', 'Signal'])
            st.dataframe(df_up, use_container_width=True)
        else:
            st.write("Abhi koi breakout nahi hai.")

    with col2:
        st.header("❄️ Breakdown Stocks")
        if breakdown_list:
            df_down = pd.DataFrame(breakdown_list, columns=['Stock', 'Price', 'Low', 'Signal'])
            st.dataframe(df_down, use_container_width=True)
        else:
            st.write("Abhi koi breakdown nahi hai.")

    st.divider()
    st.header("👀 Watchlist (Levels ke beech mein)")
    df_watch = pd.DataFrame(watchdown_list, columns=['Stock', 'Price', 'Breakout Above', 'Breakdown Below'])
    st.table(df_watch)

if st.button('Scan Market Now'):
    scan_stocks()
else:
    scan_stocks()
