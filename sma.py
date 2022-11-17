import pandas as pd
import yfinance as yf
import mplfinance as mpf
import os

os.system('jupyter nbconvert --execute --clear-output SMA.ipynb ')
# from boar.running import run_notebook

# run_notebook("SMA.ipyb")

# df.to_csv(TICKER+'.csv')
df=pd.read_csv("AAPL.csv")
print(df.head())
# mpf.plot(df["2022-04-01":],savefig='fi.png')
# mpf.plot(df["2022-04-01":],savefig='fii.png')