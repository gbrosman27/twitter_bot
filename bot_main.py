import time
import tweepy


# Twitter generated keys for user identification.
consumer_key = "x4kRrcD8PSM0K3l2IXvBK5RYl"
consumer_secret = "OJhVTJrrGLCUb43jFD5ICxrwdaDnuLlEYh4HmPKpyrfToELzmR"
access_token = "351024115-irq5NUArNqxgQB8QmBX9hfrAVfyAXM4ZyEfjl67t"
access_token_secret = "ZqEsLh8lhsjpVY52p1MAUc4qHmpKhwzNEGAQPtdsydCVJ"


# User authorization to access twitter.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    """Limits the rate the app hits the twitter API."""
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Searches for a number of tweets related to python/searched query.
# search_string = "python"
# number_of_tweets = 2

# for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
#     try:
#         tweet.favorite()
#         print("That's a cool tweet.")
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break

# Follows new followers.
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     new_follows = follower.follow()
#     print(new_follows)


# Prints tweets from homepage of timeline.
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)