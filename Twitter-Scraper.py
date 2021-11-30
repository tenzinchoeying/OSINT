import tweepy
import sys
import re
import csv
import sys
from tweepy.streaming import Stream
import pandas as pd
#Gaining API access
consumer_key="Cp7mu6vtNeRgkaYTzP694fVnQ"
consumer_secret="LzQaT7T2Ak5vjOJmaa0YwOUhMV4ablV8rFjM02YwG8xgD9C07F"
access_token="785498906889113600-U1Td6cih8cJNa5H1AfjzX6t0LghLngw"
access_token_secret="BvAHBbGgxM4rx6kMlQAdzCHIbRbUHcvB171fi1hCS4BTb"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if (not api):
    print("Authentication failed!")
    sys.exit(-1)
else:
    print("Success")

userID = input('Enter Twitter ID:')
#userID = "HoneyPyLog"
tweets = api.user_timeline(screen_name=userID, 
                           count=200,
                           include_rts = False)  #Can only retreive 200 tweets at one time
print("Number of Tweets Extracted: {}.\n".format(len(tweets)))
#writing to CSV file
fname= 'New.csv'
with open('%s.csv' % (fname), 'w', encoding='utf-8') as file:
    w = csv.writer(file)
    w.writerow(['timestamp', 'IP'])
    
   # print(ips)

db = pd.DataFrame(columns=['Tweet created', 'IP Found'])
for tweet in tweets[:200]:
    content = tweet.text #print (tweet.created_at)
    ips = re.findall(r'(\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b)', content)    #performing regex of IP
    ith_tweet = [content,ips]
    db.loc[len(db)] = ith_tweet
    db.to_csv(fname) #appending to CSV file

