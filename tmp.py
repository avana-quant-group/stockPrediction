import os 
import download
file="static/stock_data/"
print("")
print(os.getcwd())
files = os.listdir(file)
print('AAPL.csv' in files)

print(files)
from dotenv import load_dotenv

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

findfile("FB")



def findfile1(ticker):
    tic=ticker+".csv"
    file="static/stock_data/"
    files = os.listdir(file)
    print(files)
    print(tic in files)
    print(tic)
    if (tic in files) == True :
        print("HI")
       

# findfile("TSLA")
# findfile1("TSLA")
def updateticker(ticker):

    file1 = open(".env", "w") 
    s = ticker
    file1.write(s)
    file1.close() 

# updateticker("TSLA")

def read():
    f=open(".env","r")
    fw=str(f.read())
    f.close
    print(fw)

import lstm
lstm.train("FB")
