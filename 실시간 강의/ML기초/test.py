import yfinance as yf
import pandas as pd

data = yf.download('AAPL', period='5y')
data = pd.DataFrame(data)
data.reset_index(inplace=True)

def load_stock_data(ticker):
    data = yf.download(ticker, period="5y")
    data = pd.DataFrame(data)
    data.reset_index(inplace=True)
    return data.copy()