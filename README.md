# extract-text-from-google-immersive-product-api-images
Extract Text from Images in Google Immersive Product API using Python

Code examples for blog post: Analyze Text in Product Images from Google Immersive Product API using Python

You can read the blog post here: serpapi.com/blog/analyze-text-in-product-images-from-google-immersive-product-api-using-python

---

**Getting Started With Using SerpApi**

You can use our APIs in multiple languages, but for the purposes of this blog post, I've used Python.

To begin scraping data, first, create a free account on serpapi.com. You'll receive 250 free search credits each month to explore the API.

Get your SerpApi API Key from this page: https://serpapi.com/manage-api-key. 

Set your API key in an environment variable, instead of directly pasting it in the code. For this tutorial, I have saved the API key in an environment variable named "SERPAPI_API_KEY" in my .env file. [Optional but Recommended]

Next, on your local computer, you need to install a couple libraries:

`pip install google-search-results Pillow pytesseract nltk wordcloud matplotlib`

We'll also need to install Tesseract OCR itself. The installation process will depend on your operating system. For MacOS, you can use `brew install tesseract`.

---

**Run The Code**

Head to the project folder and run the code file using `python extract_text_from_google_immersive_product_images.py`

---

**Sample Output**

For a Product: LG OLED evo G4 Series Smart TV 4K

immersive_product_page_token: `eyJlaSI6IkpqZmNhTFduQl9tWXdia1A3ZGFvdUFRIiwicHJvZHVjdGlkIjoiIiwiY2F0YWxvZ2lkIjoiMTM4MTQwNzg5ODUwMzQyNTYyNiIsImhlYWRsaW5lT2ZmZXJEb2NpZCI6IjgzMTQ2NTIyMzUwMzE1ODg5MjYiLCJpbWFnZURvY2lkIjoiNjUwODQ1MDc2OTk0NDU4MDM1MSIsInJkcyI6IlBDXzM0ODgwMTQxODc4ODE3Nzk2NTR8UFJPRF9QQ18zNDg4MDE0MTg3ODgxNzc5NjU0IiwicXVlcnkiOiJMRytPTEVEK2V2bytHNCtTZXJpZXMrU21hcnQrVFYrNEsiLCJncGNpZCI6IjM0ODgwMTQxODc4ODE3Nzk2NTQiLCJtaWQiOiI1NzY0NjI3ODM3Nzc5MTUzMTMiLCJwdnQiOiJoZyIsInV1bGUiOm51bGwsImdsIjoidXMiLCJobCI6ImVuIiwiZW5naW5lIjoiZ29vZ2xlX3Nob3BwaW5nIn0=`

<img width="879" height="697" alt="Screenshot 2025-09-30 at 1 44 56 PM" src="https://github.com/user-attachments/assets/30710a4f-958b-4068-b2ff-b6fe98b56262" />



