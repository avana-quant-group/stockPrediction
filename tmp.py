import os
file="static/stock_data/"
print("")
print(os.getcwd())
files = os.listdir(file)
print('AAPL.csv' in files)

print(files)
from dotenv import load_dotenv

load_dotenv()
ticker="AAPL"
cmd="dotenv set ticker " + ticker
# print(cmd)
os.system(cmd)
print(os.getenv("ticker"))