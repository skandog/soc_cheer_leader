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



