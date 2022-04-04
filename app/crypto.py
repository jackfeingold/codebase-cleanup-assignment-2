


print("CRYPTO REPORT...")

import os
import json
from dotenv import load_dotenv
import requests
from app.utils import to_usd
from app.alphavantage_service import fetch_data


symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
#load_dotenv()

#ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

#url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
#response = requests.get(url)
#parsed_response = json.loads(response.text)
#print(parsed_response)
#breakpoint()


tsd = fetch_data(symbol)["Time Series (Digital Currency Daily)"]

dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]
#print(latest)
# not sure about the difference between '4a. close (USD)' and '4b. close (USD)'

print(symbol)
print(latest_date)
print(latest['4a. close (USD)'])
print(to_usd(float(latest['4a. close (USD)'])))
