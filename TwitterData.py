import pandas as pd
import tweepy
import configparser
import datetime

# read credentials config file
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
# print(api_key) this is a confirmation that the credentials work
# authentication process

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# obtaining tweets from a specific account

userid = 34317032
limit = 20
StartDate = datetime.datetime(2017, 1, 1, 0, 0, 0)
EndDate = datetime.datetime(2022, 2, 20, 0, 0, 0)
# if we want more than 200 tweets then we need to alter the code
# ---- this works for under 200
# tweets =api.user_timeline(screen_name = user, count = limit, tweet_mode = 'extended')

tweets = tweepy.Cursor(api.user_timeline, user_id=userid,
                       count=200, tweet_mode='extended').items(limit)

# create DataFrame
columns = ['UserID', 'User', 'Tweets', 'Time', 'Reply_To', 'Quote',
           'Retweet_Count', 'Favourite_Count',
           'Entities', 'Retweeted_By_Author', 'Language']
data = []

for tweet in tweets:
    # print(dir(tweet)) ----- gives back the directory of available attributes
    # print(tweet.full_text)
    #  if EndDate > tweet.created_at > StartDate: ---- not working atm
        data.append([tweet.user.id, tweet.user.screen_name, tweet.full_text,
                     tweet.created_at, tweet.in_reply_to_screen_name,
                     tweet.is_quote_status, #tweet.retweeted_status returns a mistake,
                     tweet.retweet_count, tweet.favorite_count,
                     tweet.entities, tweet.retweeted, tweet.lang])

df = pd.DataFrame(data, columns=columns)

print(df)
