# Like bot for Twitter, using Python and Tweepy
# Author: Bea Lorzano
# Date: October 8, 2021

import tweepy
from time import sleep
# Get keys from Twitter API
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Where q='#example', change #example to whatever Hashtag or keyword you want to search.
# Where items(100), change 100 to the amount of Tweets you want to Like.
for tweet in tweepy.Cursor(api.search, q='#example').items(100):
    try:
        print('\nLike Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to Like.')

        tweet.favorite()
        print('Like Bot successful!')

        # Where sleep(60), sleep is measured in seconds.
        # Change 60 to amount of seconds you want to have in-between Likes.
        sleep(60)

    # Will print why Tweepy could have failed in liking a Tweet:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break