#!/usr/local/bin/python2

#################### IMPORTS #####################

import string
import pandas as pd
from nltk.corpus import stopwords

from dnnsent.sentiment import sentiment_score
from twitterize import preprocess

#################### CONFIG ######################

to_process = False
full = False

################### FUNCTIONS ####################


def process(series, full=False):

    # Preprocess data
    preprocessed = series.apply(preprocess)

    # Process stop words
    if full is True:
        stop = list(string.punctuation) + ['rt', 'via'] + stopwords.words('english')
    else:
        stop = list(string.punctuation) + ['rt', 'via']

    processed = preprocessed.apply(lambda x: [item for item in x if item.lower() not in stop])

    # Rejoin into string
    processed = processed.apply(lambda x: ' '.join(x))

    return processed


##################### MAIN #######################


# Read classified dataset
df = pd.read_csv('data/trump_classified.csv')

if to_process:
    df['processed'] = process(df['4'].astype(unicode), full)
else:
    df['processed'] = df['4'].astype(unicode)

# Apply sentiment analysis
df['sentiments'] = df['processed'].apply(sentiment_score)
df.to_csv('predictions/prd_trump_classified.csv')


# Read training dataset
df2 = pd.read_csv('data/trump_unclassified.csv')

if to_process:
    df2['processed'] = process(df2['Text'].astype(unicode), full)
else:
    df2['processed'] = df2['Text'].astype(unicode)

# Apply sentiment analysis
df2['sentiments'] = df2['processed'].apply(sentiment_score)
df2.to_csv('predictions/prd_trump_unclassified.csv')
