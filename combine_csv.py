import pandas as pd
import os

data = pd.DataFrame()
dir = 'E:/Jupyter/Sollers_College/Pankaj/NLP_Sentiment_BloombergNews/NLP_News/ok/'
dfs = []

for csv_file in os.listdir(dir):
    data_temp = pd.read_csv(dir + csv_file)
    dfs.append(data_temp)

data = pd.concat(dfs)
print("Total number of news: ")
print(data.shape)
print("------------------------------------------------")
data.drop_duplicates(subset='Title', keep='first', inplace=True)
print("Total number of news (no-duplicated): ")
print(data.shape)
data.to_csv(dir + 'bloomberg_news.csv', index=False)