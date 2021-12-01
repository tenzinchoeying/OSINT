import pandas as pd
import tweepy

#Scraping function
def scrape(words, date_since, numtweet):

    # Creating DataFrame using pandas
    db = pd.DataFrame(columns=['username', 'location', 'totaltweets', 'retweetcount', 'text', 'hashtags'])
    
    # We are using .Cursor() to search through twitter for the required tweets.
    # The number of tweets can be restricted using .items(number of tweets)
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en",
                        since_id=date, tweet_mode='extended').items(numtweet)

# .Cursor() returns an iterable object. Each item in the iterator has various attributes that you can access to get information about each tweet
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
        ith_tweet = [username, description, location, totaltweets, retweetcount, text, hashtext]
        db.loc[len(db)] = ith_tweet

    filename = 'scraped_tweets.csv'

# we will save our database as a CSV file.
    db.to_csv(filename)


if __name__ == '__main__':

# Enter credentials
    consumer_key= input('Enter Consumer Key:')
    consumer_secret= input('Enter Consumer Key Secret:')
    access_token= input('Enter Access Token:')
    access_token_secret= input('Enter Access Token Secret:')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    # Enter Hashtag and initial date
    print("Enter Twitter HashTag to search")
    query = input()
    print("Enter date since the Tweets are required in yyyy-mm--dd")
    date = input()
    
    # number of tweets you want to extract in one run
    numtweet = 1000
    scrape(query, date, numtweet)
    print('Scraping Complete!')