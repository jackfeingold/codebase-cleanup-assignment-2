
#file to fetch data fron alphavantage api

import os
import json
from dotenv import load_dotenv
import requests
from pandas import read_csv

def fetch_data_crypto(symbol):

    """
    This is a function that will fetch data from the AlphaVantage API in the form of a json.  
    The function will return a parsed json in a dictionary format that can be later investigated. 
    The function will look for an API key for AlphaVantage in a .env file, but will use the demo key as a default.

    To invoke the function, pass the ticker symbol into the function.  It might look something like this:

    fetch_data_crypto("BTC")

    This would return a dictionary from AlphaVantage with data about Bitcoin
    """

    load_dotenv()

    ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

    #symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    return json.loads(response.text)


def fetch_data_stocks(symbol):

    """
    This function will fetch data in the form of a csv file from the AlphaVantage API.  
    It will return a pandas dataframe object after processing the csv.

    To invoke this function, pass in a stock ticker in string form.  It may look like this:

    fetch_data_csv("AAPL")

    This will return a dataframe with information about Apple stock.
    
    """
    
    load_dotenv()

    ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

    return read_csv(url)


def fetch_data_unemployment():
    
    """
    This function will fetch historical unemployment data from the AlphaVantage API.  
    There are no arguments or parameters, but the function will return a dictionary object from the parsed json response.
    
    Simply invoke by writing:

    variable = fetch_data_unemployment()

    The variable will now contain a dictionary with historical unemployment data.
    
    """
    
    load_dotenv()

    ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

    # docs: https://www.alphavantage.co/documentation/#unemployment
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    return json.loads(response.text)