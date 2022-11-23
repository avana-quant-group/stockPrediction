import pandas as pd
import yfinance as yf
import mplfinance as mpf
import os
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import download

# def findfile(ticker):
#     tic=ticker+".csv"
#     file="static/stock_data/"
#     files = os.listdir(file)
#     print(files)
#     print(tic in files)
#     print(tic)
#     # if (tic in files) == True :
#     if (tic in files) == False :
#         print("downloading data")
#         download.yahoo(ticker)
#         print("downloaded Ticker" + ticker )


def chart(ticker):
    # findfile(ticker)
    csv = "static/stock_data/"+ticker+".csv"
    df = pd.read_csv(csv)
    df['Date'] = pd.to_datetime(df['Date'])
    df.index = pd.DatetimeIndex(df['Date'])

    # candle volume
    pic_file = os.path.join('static', 'photo')
    picture = [pic_file + '/chart_vol.png']
    extra_plot = mpf.make_addplot(df.loc["2022-09-01":, ["High", "Low"]])
    mpf.plot(df["2022-09-01":], addplot=extra_plot, savefig=picture[0], volume=True, type="candle",
             style="yahoo")
    # candle chart
    picture.append(pic_file + '/chart.png')
    mpf.plot(df["2022-09-01":], addplot=extra_plot, savefig=picture[1], type="candle", style="yahoo")

    # sma -Simple moving average with volume
    picture.append(pic_file + '/sma_vol.png')
    mpf.plot(df["2022-09-01":], type="candle", mav=(10, 20, 30), volume=True, style="yahoo", savefig=picture[2])
    # sma -Simple moving average 
    picture.append(pic_file + '/sma.png')
    mpf.plot(df["2022-09-01":], type="candle", mav=(10, 20, 30), style="yahoo", savefig=picture[3])

    picture.append(pic_file + '/simple.png')
    mpf.plot(df["2022-09-01":], type="candle", style="yahoo", savefig=picture[4])

    return picture


# sma -Simple moving average with volume
if __name__ == "__main__":
    picture = chart()
    print(picture)
