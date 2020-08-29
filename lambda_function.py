import tweepy
from messages import messagesArray
import random
import json
from os import environ


def lambda_handler(event, context):
    tweet('If you see this tweet, you must log off twitter and: ' +
        messagesArray[random.randint(0, len(messagesArray) - 1)] + '.')
        
    return {
        'statusCode': 200,
        'body': json.dumps('LogOffBot Just Tweeted')
    }


def tweet(text):
    auth = tweepy.OAuthHandler(environ['API_KEY'], environ['API_SECRET'])
    auth.set_access_token(environ['ACCESS_TOKEN'], environ['ACCESS_TOKEN_SECRET'])
    api = tweepy.API(auth)

    api.update_status(text)
