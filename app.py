from flask import Flask,render_template,url_for
import pandas as pd
import yfinance as yf
import mplfinance as mpf 
from io import BytesIO
import os
TICKER="AAPL"

app =Flask(__name__)

@app.route('/firsthome')
def index():
    return render_template('first.html')

@app.route('/')
def index1():
    return render_template('index.html')

@app.route('/sma')
def sma():
    df=pd.read_csv(TICKER+'.csv')
    
    print(os.getcwd() )
    ll=os.getcwd()
    return render_template('index.html',user_image='fi.png',l =ll)
    

if __name__ == "__main__":
    app.run(debug=True)