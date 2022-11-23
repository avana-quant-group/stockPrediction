import math
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os

pic_file = os.path.join('static', 'photo')
picture = ""





def train(ticker):
    print(ticker+"traing")
    csv = "static/stock_data/" + ticker + ".csv"
    stock_data = pd.read_csv(csv)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data.index = pd.DatetimeIndex(stock_data['Date'])
    close_prices = stock_data['Close']
    values = close_prices.values
    training_data_len = math.ceil(len(values) * 0.8)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(values.reshape(-1, 1))

    train_data = scaled_data[0: training_data_len, :]

    x_train = []
    y_train = []

    for i in range(60, len(train_data)):
        x_train.append(train_data[i - 60:i, 0])
        y_train.append(train_data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    model = keras.Sequential()
    model.add(layers.LSTM(100, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    test_data = scaled_data[training_data_len - 60:, :]
    x_test = []
    y_test = values[training_data_len:]

    for i in range(60, len(test_data)):
        x_test.append(test_data[i - 60:i, 0])

    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    model.add(layers.LSTM(100, return_sequences=False))
    model.add(layers.Dense(25))
    model.add(layers.Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size=1, epochs=3)
    file = "static/models/" + ticker + ".h5"
    model.save(file)
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    rmse = np.sqrt(np.mean(predictions - y_test) ** 2)
    data = stock_data.filter(['Close'])
    train = data[:training_data_len]
    validation = data[training_data_len:]
    validation['Predictions'] = predictions
    plt.figure(figsize=(16, 8))
    plt.title('LSTM  Training model')
    plt.xlabel('Date')
    plt.ylabel('Close Price USD ($)')
    plt.plot(train)
    plt.plot(validation[ 'Predictions'])
    plt.legend(['Train', 'Predictions'], loc='lower right')
    # plt.show()
    picture = pic_file + '/lstmtrain.png'
    plt.savefig(picture)
    return picture



def predict(ticker):
    print("creating model")
    model = "static/models/" + ticker + ".h5"
    csv = "static/stock_data/" + ticker + ".csv"
    model = tf.keras.models.load_model(model)
    stock_data = pd.read_csv(csv)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data.index = pd.DatetimeIndex(stock_data['Date'])
    close_prices = stock_data['Close']
    values = close_prices.values
    training_data_len = math.ceil(len(values) * 0.8)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(values.reshape(-1, 1))

    train_data = scaled_data[0: training_data_len, :]

    x_train = []
    y_train = []

    for i in range(60, len(train_data)):
        x_train.append(train_data[i - 60:i, 0])
        y_train.append(train_data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    test_data = scaled_data[training_data_len - 60:, :]
    x_test = []
    y_test = values[training_data_len:]

    for i in range(60, len(test_data)):
        x_test.append(test_data[i - 60:i, 0])
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    predictions = model.predict(x_test)
    predictions = scaler.inverse_transform(predictions)
    rmse = np.sqrt(np.mean(predictions - y_test) ** 2)
    data = stock_data.filter(['Close'])
    train = data[:training_data_len]
    validation = data[training_data_len:]
    validation['Predictions'] = predictions
    plt.figure(figsize=(16, 8))
    plt.title('LSTM  Training model')
    plt.xlabel('Date')
    plt.ylabel('Close Price USD ($)')
    plt.plot(train)
    plt.plot(validation[ 'Predictions'])
    plt.legend(["normal_data",'Predictions'], loc='lower right')
    # plt.show()
    picture = pic_file + '/lstm.png'
    plt.savefig(picture)
    return picture

def predict1(ticker):
    print("creating model")
    model = "static/models/" + ticker + ".h5"
    csv = "static/stock_data/" + ticker + ".csv"
    model = tf.keras.models.load_model(model)
    stock_data = pd.read_csv(csv)
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data.index = pd.DatetimeIndex(stock_data['Date'])
    close_prices = stock_data['Close']
    values = close_prices.values
    training_data_len = math.ceil(len(values))

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(values.reshape(-1, 1))

    train_data = scaled_data[0: training_data_len, :]

    x_train = []
    y_train = []

    for i in range(60, len(train_data)):
        x_train.append(train_data[i - 60:i, 0])
        y_train.append(train_data[i, 0])

    x_train, y_train = np.array(x_train), np.array(y_train)

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    predictions = model.predict(x_train)
    predictions = scaler.inverse_transform(predictions)
    rmse = np.sqrt(np.mean(predictions - y_train) ** 2)

    data = stock_data.filter(['Close'])
    train = data[:training_data_len]
    predict = pd.DataFrame(predictions)
    plt.figure(figsize=(16, 8))
    plt.title('LSTM prediction')
    plt.ylabel('Close Price USD ($)')
    plt.plot(predict)
    # plt.legend(['Predictions'], loc='lower right')
    # plt.show()
    picture = pic_file + '/lstm.png'
    plt.savefig(picture)
    return picture
    # plt.savefig('/lstm.png')


if __name__ == "__main__":
    t1 = predict()
    print(t1)

    # train()

    # model.summary()
