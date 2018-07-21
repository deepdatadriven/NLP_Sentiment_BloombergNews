# from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

sid = SentimentIntensityAnalyzer()

def analyze(file, path):
    df = pd.read_csv(file)
    print("There are " + str(df.shape) + ' news!!')
    df['positive'] = np.nan
    df['negative'] = np.nan
    df['neutral'] = np.nan
    df['compound'] = np.nan
    columns = ['Title', 'topic', 'abstract', 'context']

    num = 0
    for idx, data in df.iterrows():
        num += 1
        corpus = ''
        for column in columns:
            if data[column] is not np.nan:
                corpus = corpus + ' '
                corpus = corpus + data[column]
            else:
                continue

        sent_scores = sid.polarity_scores(str(corpus))
        df.loc[idx, 'positive'] = sent_scores['pos']
        df.loc[idx, 'negative'] = sent_scores['neg']
        df.loc[idx, 'neutral'] = sent_scores['neu']
        df.loc[idx, 'compound'] = sent_scores['compound']

        if num % 1000 == 0:
            print('number of ' + str(num) + " news is done!!")

    df.to_csv(path + 'bloomberg_news_sentiment.csv', index=False)

if __name__ == '__main__':
    path = 'E:/Jupyter/Sollers_College/Pankaj/NLP_Sentiment_BloombergNews/NLP_News/'
    file = path + 'bloomberg_news.csv'
    analyze(file, path)