import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'GB7AYnSZX1Pb3DQdxp7xOZHZS'
consumer_secret = 'o1ty5cPVQrCFJndkmqrZ3NeXqklXi3woXmmU4IsX8bgjFhLcyp'
access_token = '1057180121210089472-I4kna5fxopUbNVijVrFzatAGN4SclZ'
access_token_secret = 'H2orr1varCAE6cDT1reMyc4Bl7xAc6z0OzLJjUplrBrJW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# Open/Create a file to append data
counter = 1
#csvFile = open('tweetersnotime.csv', 'a')
#Use csv Writer
#csvWriter = csv.writer(csvFile)
tweetcounter = 1
tweetdict = {}

tweetList = []

for tweet in tweepy.Cursor(api.search,q="#Tesla",count=100,lang="en",since="2017-04-03").items():
    #print (tweet.created_at, tweet.text)
    tweetDict = { 
                'Timestamp' : tweet.created_at,
                'Tweet' : tweet.text
    }
    #tweetdict = { tweet.created_at : tweet.text.encode('utf-8')}

    tweetList.append(tweetDict)

    
#16453 tweets in total
for i in tweetList :
    print (i)
    print ("\n")

    tweetcounter+=1


print ("Total tweets : ",tweetcounter)

#csvFile.close()
