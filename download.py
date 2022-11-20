import yfinance as yf

def yahoo(ticker):
    Ticker='MSFT' 
    start="2016-01-01"
    end="2022-11-18"
    df=yf.download(Ticker, start, end)
    return "done"