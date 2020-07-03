import tweepy

# Twitter generated keys.
consumer_key = "x4kRrcD8PSM0K3l2IXvBK5RYl"
consumer_secret = "OJhVTJrrGLCUb43jFD5ICxrwdaDnuLlEYh4HmPKpyrfToELzmR"
access_token = "351024115-irq5NUArNqxgQB8QmBX9hfrAVfyAXM4ZyEfjl67t"
access_token_secret = "ZqEsLh8lhsjpVY52p1MAUc4qHmpKhwzNEGAQPtdsydCVJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)