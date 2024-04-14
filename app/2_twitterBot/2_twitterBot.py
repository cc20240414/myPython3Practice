import tweepy
from time import sleep
from tweet_credentials import *

# Project idea is referenced from https://www.geeksforgeeks.org/how-to-make-a-twitter-bot-in-python/
# tweepy module detail: https://docs.tweepy.org/en/stable/index.html
# tweepy version: 4.14.0

"""
For FREE plan:
- Can access to X API v2 (Only Tweet creation)
- Can Access to standard v1.1 (Only Media Upload, Help, Rate Limit, and Login with X)

Reference: https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api
"""

# OAuth 1.0a User Context for Twitter API v1
auth = tweepy.OAuth1UserHandler(
   consumer_key, 
   consumer_secret,
   access_token, 
   access_token_secret
)
apiv1 = tweepy.API(auth)

# OAuth 1.0a User Context for Twitter API v2
apiv2 = tweepy.Client(
    access_token=access_token,
    access_token_secret=access_token_secret,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret)


# print(apiv1.rate_limit_status())

print("Create tweet...")
image = apiv1.simple_upload(filename='./testing.png')
media_ids = [image.media_id]
response = apiv2.create_tweet(text='This tweet is created using tweepy API', media_ids=media_ids)
print("Done. Wait 10 seconds...")
sleep(10) # 10 seconds
print("Delete tweet...")
apiv2.delete_tweet(id=response.data['id'])

print("Done.")