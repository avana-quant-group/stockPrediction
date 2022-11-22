from flask import Flask, render_template, url_for, redirect,flash,request
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd
import yfinance as yf
import mplfinance as mpf
from io import BytesIO
import os
import lstm
import sma
from dotenv import load_dotenv

load_dotenv()

TICKER = "AAPL"

app = Flask(__name__)

def getticker():
    global TICKER
    TICKER = os.getenv("ticker")

def updateticker(ticker):
    cmd = "dotenv set ticker " + ticker
    os.system(cmd)
    # os.system("dotenv set ticker" + ticker)
    getticker()


class NameForm(FlaskForm):
    name = StringField("What is your Name", validators=[DataRequired()])
    submit = SubmitField("submit")


class NameForm1(FlaskForm):
    name = StringField("Enter stock Ticker", validators=[DataRequired()])
    submit = SubmitField("submit")


@app.route('/firsthome')
def index():
    return render_template('first.html')


@app.route("/ticker")
def table():
    # converting csv to html
    data = pd.read_csv('stock.csv')
    return render_template('tiker.html', tables=[data.to_html()], titles=[''])


@app.route('/in')
def index1():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def index2():
    name = None
    form = NameForm1()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        print(name)
        # global TICKER
        TICKE = name.upper()
        updateticker(TICKE)
        print(TICKE)
        form.name.data = ''
        return redirect(url_for("sma1"))
        # flash("Form Submitted Successfully!")

    # print(name)

    return render_template("index2.html", name=name, form=form)


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/sma')
def sma1():
    pic = sma.chart(TICKER)
    pic.append(lstm.predict(TICKER))
    return render_template('sma.html', pic=pic)


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        print(name)
        form.name.data = ''
        # flash("Form Submitted Successfully!")

    # print(name)

    return render_template("name.html", name=name, form=form)


# downloading route
@app.route("/download", methods=['GET', 'POST'])
def down():
    name = None
    form = NameForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        ticker = name.upper()
        print(ticker)
        form.name.data = ''
        import download
        download.yahoo(ticker)

    return render_template('download.html', name=name, form=form)


if __name__ == "__main__":
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.run(debug=True)
    ticker()
