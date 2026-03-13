import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stock Breakout Scanner", layout="wide")
st.title("🚀 Intraday Breakout & Breakdown Scanner")
st.write("Ye scanner Nifty ke top stocks ko scan karke breakout levels batata hai.")

# List of Stocks
stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'INFY.NS', 'BHARTIARTL.NS', 'SBIN.NS', 'ITC.NS', 'ADANIENT.NS', 'TATAMOTORS.NS']

def scan_stocks():
    breakout_list = []
    breakdown_list = []
    watchlist = []

    for symbol in stocks:
        # 2 din ka data taaki kal ka high/low mil sake
        data = yf.download(symbol, period='2d', interval='5m', progress=False)
        
        if len(data) >= 2:
            # Latest price
            current_price = float(data['Close'].iloc[-1])
            
            # Kal ke data se High aur Low nikalna
            # Sabhi columns ko simple numbers mein convert kiya
            prev_day_data = data.iloc[:-1] 
            prev_high = float(prev_day_data['High'].max())
            prev_low = float(prev_day_data['Low'].min())
            
            if current_price > prev_high:
                breakout_list.append([symbol, current_price, prev_high, "🚀 BREAKOUT"])
            elif current_price < prev_low:
                breakdown_list.append([symbol, current_price, prev_low, "📉 BREAKDOWN"])
            else:
                watchlist.append([symbol, current_price, prev_high, prev_low])

    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("🔥 Breakout Stocks")
        if breakout_list:
            st.table(pd.DataFrame(breakout_list, columns=['Stock', 'Price', 'High', 'Signal']))
        else:
            st.info("Abhi koi breakout nahi mila.")

    with col2:
        st.header("❄️ Breakdown Stocks")
        if breakdown_list:
            st.table(pd.DataFrame(breakdown_list, columns=['Stock', 'Price', 'Low', 'Signal']))
        else:
            st.info("Abhi koi breakdown nahi mila.")

    st.divider()
    st.header("👀 Watchlist (Nifty Top 10)")
    if watchlist:
        st.table(pd.DataFrame(watchlist, columns=['Stock', 'Price', 'Buy Above', 'Sell Below']))

if st.button('Scan Market Now'):
    scan_stocks()
else:
    scan_stocks()
