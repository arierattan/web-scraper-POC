import streamlit as st
import sqlite3

def get_image_data():
    conn = sqlite3.connect('data/metadata.db')
    cursor = conn.cursor()
    cursor.execute('SELECT url, local_path, ocr_text FROM images')
    data = cursor.fetchall()
    conn.close()
    return data

st.title("Scraped Images and OCR Results")

image_data = get_image_data()

for url, local_path, ocr_text in image_data:
    st.image(local_path, caption=f"Image URL: {url}")
    st.text(f"OCR Text: {ocr_text}")

