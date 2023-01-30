# import tweepy
import tweepy as tw

# your Twitter API key and API secret
my_api_key = "dX05vwvhX3Vts7sCAFSmoOGNh"
my_api_secret = "ajr7KNPZwXMhlMJAeNAjihFAq31i9rVSQOqhiIWqsVLSYhXHV0"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)
search_query = "#covid19 -filter:retweets"

# get tweets from the API
tweets = tw.Cursor(api.get_status,
                   q=search_query,
                   lang="en",
                   since="2020-09-16").items(50)

# store the API responses in a list
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)

print("Total Tweets fetched:", len(tweets_copy))