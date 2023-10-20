import pandas as pd
import requests

URL = "https://api.binance.com/api/v3/ticker/24hr"
FILE = 'binance_ticker.csv'

response = requests.get(url=URL)

if response.status_code == 200:     # When Successful
    data = response.json()
    df = pd.DataFrame(data)

    #Columns to track from the API
    trackers = ["symbol", "priceChangePercent", "openPrice", "highPrice", "lowPrice", "count"]
    df = df[trackers]

    #Converting dataframe into CSV
    df.to_csv(FILE)

    print(f"{FILE} Created!")

else:
    print("Error Encountered!", response.status_code)
    
