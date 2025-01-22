import tweepy
import pandas as pd
import json
import datetime as datetime
#import s3fs

# Twitter API credentials
bearer_token = "bearer_token"


# Twitter authentication
client = tweepy.Client(bearer_token=bearer_token)



#function to handle rate limit and fetch tweets

def fetch_user_tweets(username, bucket_name):
    try:
        user = client.get_user(username=username, user_fields = ['username'])

        # Ensure the user exists
        if user.data:
            user_details = {
                'screen_name': user.data.username
            }
            if user.data:
                print(f"Fetched User: {user.data}")
                tweets = client.get_users_tweets(id=user.data.id,
                                                max_results=5,
                                                tweet_fields = ["created_at", "public_metrics"])

                # Create a pandas dataframe
                tweets_list = []

                # Ensure the tweets exist
                if tweets.data:
                    for tweet in tweets.data:

                        refined_tweet = {
                            'user': user_details["screen_name"],
                            'tweet': tweet.text,
                            'created_at' : tweet.created_at,
                            'likes' : tweet.public_metrics["like_count"],
                            'retweets' : tweet.public_metrics["retweet_count"],
                        }

                        tweets_list.append(refined_tweet)

                df = pd.DataFrame(tweets_list)
                df.to_csv('s3://{bucket_name}/tweets.csv', index=False)
                print("Dataframe created and saved to csv")
        else:
            print("ERROR : User does not exist or tweets not found")
    except tweepy.erroes.TooManyRequests as e:
        print("Rate limit reached. Waiting for 15 minutes....")
        time.sleep(15 * 60)
        fetch_user_tweets(username)
    except Exception as e:
        print("ERROR : ", e)


# with this you have successfully fetched the tweets of a user and saved it to a csv file.         