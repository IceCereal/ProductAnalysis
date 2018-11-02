import tweepy
import csv
import pandas as pd
import ast

#Getting Creds from TOKENS
PersonalCredsRaw = open('TOKENS', 'r')
PersonalCreds = ast.literal_eval(PersonalCredsRaw.read())

consumer_key = PersonalCreds["consumer_key"]
consumer_secret = PersonalCreds["consumer_secret"]
access_token = PersonalCreds["access_token"]
access_token_secret = PersonalCreds["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
counter = 1
csvFile = open('tweeters.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Tesla",count=100,lang="en",since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    
#16453 tweets in total

csvFile.close()

