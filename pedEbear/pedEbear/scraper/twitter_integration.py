import tweepy
import os
import yaml

def load_config(config_path="pedEbear\pedEbear\config\config.yaml"):
    """
    Load the configuration file for Twitter API credentials.
    """
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def twitter_login():
    """
    Authenticate with Twitter using OAuth and return an API client.
    """
    config = load_config()

    try:
        # Authenticate with Twitter using OAuthHandler
        auth = tweepy.OAuthHandler(
            config['twitter']['api_key'], config['twitter']['api_secret_key']
        )
        auth.set_access_token(
            config['twitter']['access_token'], config['twitter']['access_token_secret']
        )
        
        # Create the API object
        api = tweepy.API(auth, wait_on_rate_limit=True)
        
        # Verify credentials
        if api.verify_credentials():
            print("Successfully authenticated with Twitter!")
        else:
            print("Authentication failed. Check your API keys and tokens.")
        
        return api
    except Exception as e:
        print(f"Error during Twitter authentication: {e}")
        return None

def search_tweets(api, keyword, count=10):
    """
    Search for tweets containing a specific keyword.
    
    Args:
        api (tweepy.API): The authenticated API object.
        keyword (str): The keyword to search for in tweets.
        count (int): The number of tweets to retrieve.
    
    Returns:
        list: A list of tweet objects.
    """
    try:
        tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(count)
        return list(tweets)
    except Exception as e:
        print(f"Error during tweet search: {e}")
        return []
