from multiprocessing import AuthenticationError
from re import search
import tweepy
import os
from dotenv import load_dotenv
import json

import time

load_dotenv()

api_key = os.environ.get("API_KEY")
api_key_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

hashtag = "theSchoolOfCode"
tweet_number = 40
omitted = ["tensorflow", "tumblr", "diagorovenko",
           "https://koukokaga", "bhubaneswar", "win", "coding", "hate", "fuck", "shit"]

tweets = tweepy.Cursor(api.search_tweets, hashtag).items(tweet_number)


# def string_filter(omit, string):
#     for x in omit:
#         if any(x in string):
#             print(x)
#             return False
#         else:
#             print(x)
#             return True


# print(string_filter(["ff", "gg"], "jjgkldfop tensorflow"))

def search_bot(hashtag, tweet_number):

    #    omitted = ["tensorflow", "tumblr", "diagorovenko",
    #           "https://koukokaga", "bhubaneswar", "win", "coding", "hate", "fuck", "shit"]

    tweets = tweepy.Cursor(api.search_tweets, hashtag).items(tweet_number)

    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            print("retweeted: " + tweet.text)
            time.sleep(60)
        except tweepy.TweepyException as e:
            print(e)
            time.sleep(2)


while True:
    search_bot("#100DaysOfCode", 50)
    time.sleep(600)
    search_bot("@theschoolofcode", 20)
    time.sleep(600)
    search_bot("I love coding", 10)
    time.sleep(600)
