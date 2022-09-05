from multiprocessing import AuthenticationError
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

# print("hold up, my man is tweeting!")
# api.update_status("Thank you Twitter for the access, I plan to add some automation to this wee guy")

FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


# tweets = api.mentions_timeline(since_id=1565760750328627206)


def reply():
    tweets = api.mentions_timeline(
        since_id=read_last_seen(FILE_NAME), tweet_mode='extended')

    for tweet in reversed(tweets):
        if '#botlife' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name +
                              " I love being a robot, I can reply, like and retweet babyyyy", in_reply_to_status_id=tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(15)
