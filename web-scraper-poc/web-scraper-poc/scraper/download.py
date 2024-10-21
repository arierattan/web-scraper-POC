import os
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_directory):
    """
    Download an image from the given URL and save it to the specified directory.
    """
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            filename = os.path.basename(image_url)
            save_path = os.path.join(save_directory, filename)
            
            with open(save_path, 'wb') as image_file:
                image_file.write(response.content)
            
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
