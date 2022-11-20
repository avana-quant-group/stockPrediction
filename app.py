from flask import Flask,render_template,url_for
import pandas as pd
import yfinance as yf
import mplfinance as mpf 
from io import BytesIO
import os
TICKER = "AAPL"

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
    PEOPLE_FOLDER = os.path.join('static', 'photo')
    print(os.getcwd() )
    PEOPLE_FOLDER=PEOPLE_FOLDER+"/"+"fi.png"
    ll=os.getcwd()
    return render_template('sma.html',user_image=PEOPLE_FOLDER,l =ll)

@app.route("/download")
def down():
    import download
    download.yahoo()
    return render_template('sma.html')

if __name__ == "__main__":
    app.run(debug=True)