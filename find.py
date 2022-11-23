import lstm
import os
import download

def findfileh5(ticker):
    print("find file found")
    tic= ticker + ".h5"
    file= "static/models/"
    files = os.listdir(file)
    if (tic in files) == False :
        lstm.train(ticker)
        print("training")

def findfile(ticker):
    tic=ticker+".csv"
    file="static/stock_data/"
    files = os.listdir(file)
    print(files)
    print(tic in files)
    print(tic)
    # if (tic in files) == True :
    if (tic in files) == False :
        print("downloading data")
        download.yahoo(ticker)
        print("downloaded Ticker" + ticker )



        