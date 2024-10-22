from scraper.scraper import scrape_images_from_page
from scraper.download import download_image
from scraper.twitter_integration import twitter_login, search_tweets
from ocr.ocr_processing import extract_text_from_image
from data.metadata import initialize_database, store_image_metadata
import yaml

def load_config(config_path="pedEbear\pedEbear\config\config.yaml"):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    # Load configuration
    config = load_config()
    
    # Initialize the database
    initialize_database()

    # Scrape from predefined websites
    urls = config['scraper']['urls']
    for url in urls:
        print(f"Scraping images from {url}...")
        image_urls = scrape_images_from_page(url)
        for img_url in image_urls:
            local_image_path = download_image(img_url, config['storage']['images_dir'])
            if local_image_path:
                ocr_text = extract_text_from_image(local_image_path)
                store_image_metadata(img_url, local_image_path, ocr_text)
    
    # Authenticate with Twitter
    api = twitter_login()
    
    if api:
        # Search for tweets containing keywords like "passport", "ID", "license"
        keyword = "passport OR ID card OR license"
        print(f"Searching Twitter for {keyword}...")
        tweets = search_tweets(api, keyword, count=10)

        for tweet in tweets:
            tweet_content = tweet.text
            print(f"Found tweet: {tweet_content}")
            # Here, you could download images from the tweet and process them
            if 'media' in tweet.entities:
                for media in tweet.entities['media']:
                    media_url = media['media_url']
                    local_image_path = download_image(media_url, config['storage']['images_dir'])
                    if local_image_path:
                        ocr_text = extract_text_from_image(local_image_path)
                        store_image_metadata(media_url, local_image_path, ocr_text)
                        print(f"Stored metadata for {local_image_path}")
            else:
                print("No media found in the tweet.")
    else:
        print("Twitter login failed. Skipping Twitter scraping.")

if __name__ == "__main__":
    main()
