import tweepy
import csv


consumer_key = 'y4Rd64OAuRMuf2OoXBq7XoC8k'      # these are our keys for accessing Twitter API
consumer_secret = 'KoO8UZzPTSWuhj5TxEEwXyAu0H5s1hEMCQVmNAUj7F3ceQ1ecA'
access_token = '2744457040-J3p1VJSmaAErN09Ukdm8y4rrU4N38ZhGUah6hJv'
access_secret = 'tbWFGA5D28KKkzYkoN6WA80fXdi8aKX73MNcS2Kx6iOVV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


def get_all_tweets(screen_name):

    alltweets = []  # all 3240 tweets will be hold in this array

    new_tweets = api.user_timeline(screen_name=screen_name, count=200) # get most recent 200 tweets

    alltweets.extend(new_tweets)    # adding them to list

    oldest = alltweets[-1].id - 1   # last tweet's id - 1 for continuing from there

    while len(new_tweets) > 0:      # get tweets until there is no left

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        alltweets.extend(new_tweets) # keep extending the list

        oldest = alltweets[-1].id - 1

    outtweets = [[tweet.text.encode('ascii', 'ignore')] for tweet in alltweets] # encoding tweets for csv

    with open('%s_tweets.csv' % screen_name, 'w') as f: # writing to csv
        writer = csv.writer(f)
        writer.writerows(outtweets)


get_all_tweets("ubisoft")           # <------ here write the username you want
