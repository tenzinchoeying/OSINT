import pandas as pd
import tweepy

#Scraping function
def scrape(words, date_since, numtweet):

    # Creating DataFrame using pandas
    db = pd.DataFrame(columns=['username', 'location', 'totaltweets', 'retweetcount', 'text', 'hashtags'])
    
    # We are using Cursor() to search through twitter for the required tweets.
    # The number of tweets can be restricted using .items(number of tweets)
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en",
                        since_id=date, tweet_mode='extended').items(numtweet)

# Cursor returns an iterable object. Each item in the iterator has various attributes that you can access to get information about each tweet
    list_tweets = [tweet for tweet in tweets]

# Counter to maintain Tweet Count
    i = 1

#Extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        location = tweet.user.location
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
    
# Retweets can be distinguished by a retweeted_status attribute
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

# Appending all the extracted information in the DataFrame
        ith_tweet = [username, location, totaltweets, retweetcount, text, hashtext]
        db.loc[len(db)] = ith_tweet

    filename = 'scraped_tweets.csv'

# we will save our database as a CSV file.
    db.to_csv(filename)

def hashScrape(key_var, sKey_var,token_var, sToken_var, hashtag_var, date_var)
    if __name__ == '__main__':

    # Enter credentials
        consumer_key= key_var
        consumer_secret= sKey_var
        access_token= token_var
        access_token_secret= sToken_var
        
        print('Enter Consumer Key:' + consumer_key)
        print('Enter Consumer Key Secret:' + consumer_secret)
        print('Enter Access Token:' + access_token)
        print('Enter Access Token Secret:' + access_token_secret)

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        
        # Enter Hashtag and initial date
        query = hashtag_var
        print("Enter Twitter HashTag to search:" + query)
        date = date_var
        print("Enter date since the Tweets are required in yyyy-mm--dd" + date)
        
        # number of tweets you want to extract in one run
        numtweet = 2000
        scrape(query, date, numtweet)
        print('Scraping Complete!')
