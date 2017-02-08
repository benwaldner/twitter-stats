import pandas as pd

df = pd.read_csv("trump_full.csv")
df.head()
df.shape

df2 = df

df2['Text'] = df2['Text'].map(lambda x: str(x)[:-1])
df2['Text'] = df2['Text'].map(lambda x: str(x)[2:])

df2.head()
df2.to_csv('trump_unclassified.csv')
