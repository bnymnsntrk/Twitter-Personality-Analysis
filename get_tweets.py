import tweepy
import csv
import prepare_data
import test

consumer_key = 'y4Rd64OAuRMuf2OoXBq7XoC8k'
consumer_secret = 'KoO8UZzPTSWuhj5TxEEwXyAu0H5s1hEMCQVmNAUj7F3ceQ1ecA'
access_token = '2744457040-J3p1VJSmaAErN09Ukdm8y4rrU4N38ZhGUah6hJv'
access_secret = 'tbWFGA5D28KKkzYkoN6WA80fXdi8aKX73MNcS2Kx6iOVV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print
        "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print
        "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [[tweet.text.encode('ascii', 'ignore')] for tweet in alltweets]

    # write the csv	
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)

    pass

    # pass in the username of the account you want to download
    # get_all_tweets("realdonaldtrump")
