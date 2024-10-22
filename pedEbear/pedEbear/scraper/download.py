import os
import requests
from PIL import Image
from io import BytesIO
from urllib.parse import urlparse

def download_image(image_url, save_directory):
    """
    Download an image from the given URL and save it to the specified directory.
    Strips query parameters from the URL when saving the file.
    
    Args:
        image_url (str): The URL of the image to download.
        save_directory (str): The directory where the image will be saved.
        
    Returns:
        str: The path where the image was saved, or None if the download failed.
    """
    try:
        # Parse the image URL to remove query parameters
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)
        
        # Ensure the save directory exists
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        
        # Full path to save the image
        save_path = os.path.join(save_directory, filename)
        
        # Download the image content
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as image_file:
                for chunk in response.iter_content(1024):
                    image_file.write(chunk)
            print(f"Downloaded {image_url} to {save_path}")
            return save_path
        else:
            print(f"Failed to download {image_url} - Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading {image_url}: {e}")
        return None
def download_images(image_urls, save_directory):
    """
    Download multiple images and save them to the specified directory.
    """
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    for image_url in image_urls:
        download_image(image_url, save_directory)
