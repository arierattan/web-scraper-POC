from scraper.scraper import scrape_images_from_page
from scraper.download import download_images
from ocr.ocr_processing import extract_text_from_image
from data.metadata import initialize_database, store_image_metadata


def main():
    # Initialize the database (run this once)
    initialize_database()

    # Define the webpage URL to scrape
    url = "https://en.wikipedia.org/wiki/Identity_document"  # Replace with the real URL

    # Scrape images from the page
    print(f"Scraping images from {url}...")
    image_urls = scrape_images_from_page(url)
    print(f"Found {len(image_urls)} images.")

    # Download images to the local storage directory
    if image_urls:
        print("Downloading images...")
        download_images(image_urls, "storage/images")
        print("Download completed.")

        # Process each image and extract text using OCR
        for img_url in image_urls:
            local_image_path = f"storage/images/{img_url.split('/')[-1]}"
            ocr_text = extract_text_from_image(local_image_path)
            
            # Store image metadata in the database
            store_image_metadata(img_url, local_image_path, ocr_text)
            print(f"Stored metadata for {local_image_path}")

if __name__ == "__main__":
    main()
