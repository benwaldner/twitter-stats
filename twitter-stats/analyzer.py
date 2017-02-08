#################### IMPORTS #####################

import string
import pandas as pd
from nltk.corpus import stopwords

from dnnsent.sentiment import sentiment_score
from downloader import download_tweets
from tokenizer import preprocess

#################### CONFIG ######################

user = 'realDonaldTrump'
file1 = 'data/' + user + '.csv'
file2 = 'data/pred/' + user + '.csv'

full_process = False

################### FUNCTIONS ####################


def process(series, full_process=False):

    # Preprocess data
    preprocessed = series.apply(preprocess)
    base_stop_words = list(string.punctuation) + ['rt', 'via']

    # Process stop words or not
    if full_process: stop = base_stop_words + stopwords.words('english')
    else: stop = base_stop_words

    # Remove stop words
    processed = preprocessed.apply(lambda x: [item for item in x if item.lower() not in stop])

    return processed


def get_sentiment():

    # Download dataset
    #download_tweets()

    # Read classified dataset
    df = pd.read_csv(file1, encoding='utf-8')

    # Apply sentiment analysis
    df['sentiments'] = df['Text'].astype(str).apply(sentiment_score)
    df['processed'] = process(df['Text'].astype(str), full_process)

    # Export to CSV
    df.to_csv(file2, encoding='utf-8')


##################### MAIN #######################

if __name__ == '__main__':
    get_sentiment()
