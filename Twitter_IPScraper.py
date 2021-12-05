import tweepy
import sys
import re
import csv
import sys
from tweepy.streaming import Stream
import pandas as pd

def IPScraper(key_var, sKey_var,token_var, sToken_var, id_var, num_var):
    #Gaining API access
    consumer_key= key_var
    consumer_secret= sKey_var
    access_token= token_var
    access_token_secret= sToken_var
    
    print('Enter Consumer Key:' + consumer_key)
    print('Enter Consumer Key Secret:' + consumer_secret)
    print('Enter Access Token:' + access_token)
    print('Enter Access Token Secret:' + access_token_secret)


    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    if (not api):
        print("Authentication failed!")
        sys.exit(-1)
    else:
        print("Success")

    userID = id_var
    print('Enter Twitter ID:' + userID)
    #userID = "HoneyPyLog"
    tweets = api.user_timeline(screen_name=userID, 
                               count=200,
                               include_rts = False)  #Can only retreive 200 tweets at one time
    tweets = int(num_var)
    #print("Number of Tweets Extracted: {}.\n".format(len(tweets)))
    print ("Number of Tweets Extracted:" + tweets)
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
        db.to_csv(fname)

