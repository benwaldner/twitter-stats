#################### IMPORTS #####################

import datetime
from collections import Counter

import numpy as np
import pandas as pd
import pandas_datareader.data as web

##################### MAIN #######################

df = pd.read_csv('predictions/prd_stocks_copy.csv')
df.columns
del df['altticker']
df.dropna(inplace=True)
df.index = df['0']
df

stocks = []
for i, stock in enumerate(df['ticker']):
    start = datetime.datetime.strptime(df.index[i], '%Y-%m-%d %H:%M')
    end = start + datetime.timedelta(days=7)

    stock = web.get_data_yahoo(stock, start, end)
    stocks.append(stock)

##################### TESTS ######################

#yyyy-mm-dd hh:mm:ss
