import datetime
import tweepy
import csv 
import json
# Create an app in your Twitter dev account to obtain these keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
file_name = "twitter_small.txt"

f = open(file_name,"w")

for tweet in tweepy.Cursor(api.search, q='*',tweet_mode='extended', lang='nl',
                           wait_on_rate_limit = True, wait_on_rate_limit_notify = True).items(10000):
    f.write(json.dumps(tweet._json) + '\n')

f.close()

