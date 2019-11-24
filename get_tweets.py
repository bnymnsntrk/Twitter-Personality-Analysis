import tweepy

consumer_key = 'y4Rd64OAuRMuf2OoXBq7XoC8k'
consumer_secret = 'KoO8UZzPTSWuhj5TxEEwXyAu0H5s1hEMCQVmNAUj7F3ceQ1ecA'
access_token = '2744457040-J3p1VJSmaAErN09Ukdm8y4rrU4N38ZhGUah6hJv'
access_secret = 'tbWFGA5D28KKkzYkoN6WA80fXdi8aKX73MNcS2Kx6iOVV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

"""tweets = api.home_timeline()     #get tweets from timeline
for tweet in tweets:
    print('{real_name} (@{name}) said {tweet}\n\n'.format(
        real_name=tweet.author.name, name=tweet.author.screen_name,
        tweet=tweet.text))"""

user = api.get_user('tilkioguzz')
"""print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)"""

for block in user.followers():
    print(block.name)
