import yfinance as yf
import pandas as pd
import date


# https://stackoverflow.com/questions/6757192/importing-a-function-from-a-class-in-another-file

class stock_info:

    def __init__(self,name_list):
        self.name_list=name_list


    def holdin_info_iterator(name_list):
        price_list=[]
        day_percentage_list=[]
        for i in name_list:
            ticker_symbol=i
            ticker=yf.Ticker(ticker_symbol)
            current_price = ticker.info['regularMarketPrice']
            previous_close_price = ticker.info['regularMarketPreviousClose']

            percentage_change = ((current_price - previous_close_price) / previous_close_price) * 100
            price_list.append(current_price)
            day_percentage_list.append(percentage_change)
            day_info_price_dict={}
            for i in range(len(price_list)):
                day_info_price_dict[price_list[i]]=day_percentage_list[i]
        return day_info_price_dict
    

    
    

# Calculate the percentage change


# Replace 'AAPL' with your desired stock's ticker
ticker_symbol = 'AAPL'
ticker = yf.Ticker(ticker_symbol)

# Get the current price
current_price = ticker.info['regularMarketPrice']

print(f"The current price of {ticker_symbol} is: {current_price}")

import yfinance as yf

# Replace 'AAPL' with your desired stock's ticker
ticker_symbol = 'AAPL'
ticker = yf.Ticker(ticker_symbol)

# Get the current price and previous close price
current_price = ticker.info['regularMarketPrice']
previous_close_price = ticker.info['regularMarketPreviousClose']

# Calculate the percentage change
percentage_change = ((current_price - previous_close_price) / previous_close_price) * 100

print(f"The current price of {ticker_symbol} is: {current_price}")
print(f"The percentage change since last close is: {percentage_change:.2f}%")


main:
stock_csv=pd.read_csv("")
df=pd.DataFrame(day_info_price_dict)
# add name list to the df and then to csv


# get sector name also
# and todays date
