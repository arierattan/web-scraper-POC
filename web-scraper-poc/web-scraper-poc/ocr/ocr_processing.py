import pytesseract
from PIL import Image
import os
import pytesseract

# If Tesseract isn't added to the PATH, set the path to the executable manually
# Example: For Windows, use the correct installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# For Linux or macOS, this might not be needed if installed in standard locations.

def extract_text_from_image(image_path):
    """
    Extract text from an image using OCR (pytesseract).
    
    Args:
        image_path (str): Path to the image file.
        
    Returns:
        str: The extracted text from the image.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return ""

def extract_text_from_images_in_directory(directory):
    """
    Extract text from all images in a specified directory.
    
    Args:
        directory (str): Path to the directory containing image files.
        
    Returns:
        dict: A dictionary mapping image paths to extracted text.
    """
    ocr_results = {}
    for filename in os.listdir(directory):
        image_path = os.path.join(directory, filename)
        text = extract_text_from_image(image_path)
        ocr_results[image_path] = text
        print(f"Extracted text from {filename}: {text[:50]}...")  # Print first 50 characters of the text
    return ocr_results

# Example usage
if __name__ == "__main__":
    directory = "storage/images"
    results = extract_text_from_images_in_directory(directory)
    for image, text in results.items():
        print(f"Image: {image}, Text: {text}")
