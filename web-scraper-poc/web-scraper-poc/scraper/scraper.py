import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_images_from_page(url):
    """
    Scrape all image URLs from a webpage and filter them to match identification-related keywords.
    
    Args:
        url (str): The URL of the webpage to scrape images from.
        
    Returns:
        list: A list of filtered absolute image URLs likely to be identification-related.
    """
    # Keywords to filter for identification-related images
    id_keywords = ['id', 'passport', 'license', 'identification', 'driver', 'card']

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve {url} - Status Code: {response.status_code}")
            return []

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image tags and extract the 'src' attribute
        images = soup.find_all('img')
        
        # Convert relative URLs to absolute URLs
        image_urls = [urljoin(url, img['src']) for img in images if 'src' in img.attrs]
        
        # Filter the URLs based on id-related keywords in their filename or URL
        filtered_urls = [img_url for img_url in image_urls if any(keyword in img_url.lower() for keyword in id_keywords)]

        return filtered_urls
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

# Example usage for testing
if __name__ == "__main__":
    test_url = "https://www.example.com"  # Replace with a real URL for testing
    images = scrape_images_from_page(test_url)
    print(f"Found {len(images)} identification-related images.")
    for img_url in images:
        print(img_url)


#Explanation:
# scrape_images_from_page(url): This function takes a webpage URL and scrapes all the <img> tags from the page. It returns a list of image URLs.
#requests.get(url): Fetches the HTML content of the webpage.
#BeautifulSoup: Parses the HTML and finds all image tags (<img>), extracting the src attributes.