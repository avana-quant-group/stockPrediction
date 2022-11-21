import pandas as pd
import yfinance as yf


def yahoo(Ticker="MSFT"):
    # Ticker = 'MSFT'
    start = "2016-01-01"
    end = "2022-11-18"
    df = yf.download(Ticker, start, end, auto_adjust=True)
    df = df.reset_index()
    file = "static/stock_data/" + Ticker + ".csv"

    df.to_csv(file, index=False)

    return "done"


if __name__ == "__main__":
    yahoo("AAPL")
