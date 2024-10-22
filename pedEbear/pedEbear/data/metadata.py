# data/metadata.py
import os
import sqlite3

import sqlite3
import os

def initialize_database():
    """
    Initialize the SQLite database with a table to store image metadata.
    Ensure that the 'data' directory exists before creating the database file.
    """
    # Ensure the 'data' directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    conn = sqlite3.connect('data/metadata.db')
    cursor = conn.cursor()

    # Create table to store image metadata
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            local_path TEXT,
            ocr_text TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


def store_image_metadata(url, local_path, ocr_text):
    """
    Store metadata for an image in the SQLite database.
    
    Args:
        url (str): The URL of the image.
        local_path (str): The local file path of the downloaded image.
        ocr_text (str): The text extracted from the image using OCR.
    """
    conn = sqlite3.connect('data/metadata.db')
    cursor = conn.cursor()

    # Insert image metadata into the database
    cursor.execute('''
        INSERT INTO images (url, local_path, ocr_text)
        VALUES (?, ?, ?)
    ''', (url, local_path, ocr_text))

    conn.commit()
    conn.close()
