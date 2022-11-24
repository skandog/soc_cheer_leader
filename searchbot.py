import tweepy
import os
from dotenv import load_dotenv
import random

import time

# Used only for debug in local terminal so to structure json
import json
from pprint import pprint


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
        pprint(tweet._json["user"]["followers_count"])
        # pprint(json.dumps(tweet._json,
        #                  sort_keys=True, indent=4, separators=(",", ": ")))
        if tweet._json["user"]["followers_count"] > 20:
            try:
                tweet.retweet()
                api.create_favorite(tweet.id)
                print("retweeted: " + tweet.text)
                time.sleep(10)
            except tweepy.TweepyException as e:
                print(e)
                time.sleep(2)
        else:
            print("Follower count less than 10, could be spam")


# List of possible search terms
q = ["#100DaysOfCode", "@theschoolofcode", "I love coding",
     "#python", "#dev", "#coding", "#DataScience", "#AI"]

# Randomiser to choose search term
searchterm = q[random.randint(0, len(q) - 1)]
print("Current search term: ", searchterm)

search_bot(searchterm, 25)
