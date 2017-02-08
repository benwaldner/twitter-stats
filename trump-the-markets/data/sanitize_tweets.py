import pandas as pd

df = pd.read_csv("trump_hillary.csv", header=None)

df2 = df[df[:]]

df2['Text'] = df2['Text'].map(lambda x: str(x)[:-1])
df2['Text'] = df2['Text'].map(lambda x: str(x)[2:])

df2.head()
df2.to_csv('trump_classified.csv')
