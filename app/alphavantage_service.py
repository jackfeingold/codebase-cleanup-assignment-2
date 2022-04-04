
#file to fetch data fron alphavantage api

import os
import json
from dotenv import load_dotenv
import requests


def fetch_data(symbol):

    load_dotenv()

    ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

    #symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    return json.loads(response.text)
