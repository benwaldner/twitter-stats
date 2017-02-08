#################### IMPORTS #####################

from datetime import datetime
from collections import Counter

import numpy as np
import pandas as pd
import pandas_datareader.data as web

##################### MAIN #######################

companies = open('data/companies.txt', encoding='utf-8').readlines()
companies = [company.strip() for company in companies]

df = pd.read_csv("predictions/prd_trump_unclassified.csv").head(n=10000).astype(str)
df.columns

lst = []
lst2 = []
for i, text in enumerate(df['processed'].values):
    for company in companies:

        if (company or ("@" + company)) in text.lower().split():
            print(company, df['processed'][i].lower())
            lst.append((df['Date'][i], df['processed'][i], company, df['sentiments'][i]))
            lst2.append(company)

df2 = pd.DataFrame(lst)
df2.to_csv('predictions/prd_stocks.csv')
#for i in lst: print(type(i)
print(Counter(lst2).most_common())

##################### TESTS ######################

#yyyy-mm-dd hh:mm:ss
