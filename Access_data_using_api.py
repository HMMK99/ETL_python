import pandas as pd
import requests


url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=***"
web_data = requests.get(url).text

data = pd.read_json(web_data)

data.drop(columns=['success', 'timestamp', 'base', 'date'], inplace=True)

data.to_csv('exchange_rates_1.csv')
