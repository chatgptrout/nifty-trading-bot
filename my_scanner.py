import yfinance as yf
import time

def check_market():
    ticker = "^NSEI" # Nifty 50
    print(f"Checking {ticker}...")
    
    # Live data nikalna
    data = yf.download(tickers=ticker, period='1d', interval='1m', progress=False)
    
    if not data.empty:
        # Naye format ke liye ye line update ki hai
        current_price = float(data['Close'].iloc[-1])
        print(f"Nifty Live Price: {current_price:.2f}")
        
        avg_5min = float(data['Close'].tail(5).mean())
        
        if current_price > avg_5min:
            print(">>> SIGNAL: Trend is UP (Bullish) <<<")
        else:
            print(">>> SIGNAL: Trend is DOWN (Bearish) <<<")
    else:
        print("Data nahi mil raha. Internet check karein.")

while True:
    try:
        check_market()
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 30)
    time.sleep(60)