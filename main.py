from multiprocessing import AuthenticationError
import tweepy
import os
from dotenv import load_dotenv
import json

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

tweets = api.mentions_timeline()
# print(tweets[0].text)

for tweet in tweets:
    if '#botlife' in tweet.text.lower():
        print(str(tweet.id) + ' - ' + tweet.text)
