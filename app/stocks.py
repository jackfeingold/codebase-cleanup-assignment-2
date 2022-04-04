

print("STOCKS REPORT...")

import os
from app.alphavantage_service import fetch_data_stocks
from dotenv import load_dotenv
from pandas import read_csv
from app.utils import to_usd


symbol = input("Please input a stock ticker (default: 'NFLX'): ") or "NFLX"

#load_dotenv()

#ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


#url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

#df = read_csv(url)
#print(df.columns)
#breakpoint()

latest = fetch_data_stocks(symbol).iloc[0]


print(symbol)
print(latest["timestamp"])
print(latest["close"])
print(to_usd(latest["close"]))
