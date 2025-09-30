import csv
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os
import requests, json
from PIL import Image
import pytesseract
import cv2 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
load_dotenv()
nltk.download('stopwords')

# --- Configuration ---
serpapi_api_key = os.environ["SERPAPI_API_KEY"] # Replace YOUR_SERPAPI_API_KEY if not using env var
output_image_filename = "downloaded_image.png"
immersive_product_page_token = "eyJlaSI6IkpqZmNhTFduQl9tWXdia1A3ZGFvdUFRIiwicHJvZHVjdGlkIjoiIiwiY2F0YWxvZ2lkIjoiMTM4MTQwNzg5ODUwMzQyNTYyNiIsImhlYWRsaW5lT2ZmZXJEb2NpZCI6IjgzMTQ2NTIyMzUwMzE1ODg5MjYiLCJpbWFnZURvY2lkIjoiNjUwODQ1MDc2OTk0NDU4MDM1MSIsInJkcyI6IlBDXzM0ODgwMTQxODc4ODE3Nzk2NTR8UFJPRF9QQ18zNDg4MDE0MTg3ODgxNzc5NjU0IiwicXVlcnkiOiJMRytPTEVEK2V2bytHNCtTZXJpZXMrU21hcnQrVFYrNEsiLCJncGNpZCI6IjM0ODgwMTQxODc4ODE3Nzk2NTQiLCJtaWQiOiI1NzY0NjI3ODM3Nzc5MTUzMTMiLCJwdnQiOiJoZyIsInV1bGUiOm51bGwsImdsIjoidXMiLCJobCI6ImVuIiwiZW5naW5lIjoiZ29vZ2xlX3Nob3BwaW5nIn0="
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract' # Example for macOS
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Example for Windows


# --- 1. Fetch Ad Data from Google Ads Transparency Center ---
def get_data_from_google_immersive_product(immersive_product_page_token):
    params = {
        "api_key": serpapi_api_key,
        "engine": "google_immersive_product",
        "page_token": immersive_product_page_token
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("product_results", [])

# --- 2. Download the Ad Image ---
def download_image(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image from {url}: {e}")
        return None
    
# --- 3. Extract Text from the Image using Tesseract OCR ---
def extract_text_from_image(image_path):
    try:
        img = cv2.imread(image_path)
        img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        extracted_text = pytesseract.image_to_string(img, lang='eng')
        return extracted_text
    except Exception as e:
        print(f"Error during OCR processing of {image_path}: {e}")
        return None

# --- 4. Create Word Cloud ---
def create_wordcloud(all_extracted_text):
    all_text = " ".join(all_extracted_text)
    stop_words = set(stopwords.words('english'))
    wordcloud = WordCloud(
        stopwords=stop_words,
        background_color='white',
        width=800,
        height=600,
        max_words=100,
        colormap='coolwarm'
    ).generate(all_text)
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Turn off axis labels
    plt.title("Word Cloud of Most Occurring Words in Product Images", fontsize=16)
    plt.show()

# --- Main Execution ---

if __name__ == "__main__":
    if not serpapi_api_key:
        print("Please set your SERPAPI_API_KEY environment variable or replace 'YOUR_SERPAPI_API_KEY' in the script.")
    else:
        all_extracted_text = []
        print(f"Searching Google Immersive Product for: '{immersive_product_page_token}'")
        product_data = get_data_from_google_immersive_product(immersive_product_page_token)
        if not product_data:
            print("No data found for the query.")
        else:
            found_image_ad = False
            if "thumbnails" in product_data:
                product_images = product_data["thumbnails"]
                print(f"Found {len(product_images)} images.")
                for image in product_images:
                    print(f"\n--- Processing Image ---")
                    downloaded_path = download_image(image, output_image_filename)
                    if downloaded_path:
                        print(f"Image downloaded to: {downloaded_path}")
                        extracted_text = extract_text_from_image(downloaded_path)
                        if extracted_text:
                            print("\n--- Extracted Text from Product Image ---")
                            all_extracted_text.append(extracted_text)
                        else:
                            print("Could not extract text from the image.") 
                create_wordcloud(all_extracted_text)
            else:
                print("No images found in the product data.")