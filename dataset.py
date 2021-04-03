# Import required libraries
import os
import sys
from sys import argv
import pandas as pd
from pandas.io.json import json_normalize
from zipfile import ZipFile
import warnings
warnings.filterwarnings('ignore')

# Run snscrape in CLI to get tweets
hashtag = argv[1]     # Input from user (#FarmersProtest taken as example)
if hashtag[0]=='#':
    hashtag = hashtag[1:]
results = argv[2]   # Input from user (100 taken as example)
scrape_tweets = "snscrape --jsonl --progress --max-results " + str(results) + " twitter-search \"#" + hashtag + " lang:en\" > raw_tweets.json"
os.system(scrape_tweets)

# Read JSON file containing tweets data
raw_tweets = pd.read_json('raw_tweets.json', lines=True)

# Normalize 'user' filed, remove less important fields and rename 'id' to 'userId'
users = json_normalize(raw_tweets['user'])
users.drop(['description', 'linkTcourl'], axis=1, inplace=True)
users.rename(columns={'id':'userId', 'url':'profileUrl'}, inplace=True)

# Create DataFrame, remove duplicates and save as CSV file
users = pd.DataFrame(users)
users.drop_duplicates(subset=['userId'], inplace=True)
users.to_csv('users.csv', index=None)

# Transform 'raw_tweets' DataFrame to get 'tweets' DF
# Add column for 'userId'
user_id = []
for user in raw_tweets['user']:
    uid = user['id']
    user_id.append(uid)
raw_tweets['userId'] = user_id
# Remove less important fields and rename 'id' to 'tweetId'
cols = ['url', 'date', 'renderedContent', 'id', 'userId', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount', 'source', 'media', 'retweetedTweet', 'quotedTweet', 'mentionedUsers']
tweets = raw_tweets[cols]
tweets.rename(columns={'id':'tweetId', 'url':'tweetUrl'}, inplace=True)

# Convert to DataFrame, remove duplicates and save as CSV file
tweets = pd.DataFrame(tweets)
tweets.drop_duplicates(subset=['tweetId'], inplace=True)
tweets.to_csv('tweets.csv', index=None)

# Create zip folder with tweets.csv and users.csv
zipObj = ZipFile('dataset.zip', 'w')
zipObj.write('tweets.csv')
zipObj.write('users.csv')
zipObj.close()

# Delete files
delete_files = "del raw_tweets.json tweets.csv users.csv"
os.system(delete_files)