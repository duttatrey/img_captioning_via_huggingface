from transformers import pipeline
from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())
#img2caption
def img2text(url):
    image_to_text=pipeline("image-to-text", model="Salesforce/blip-image-captioning-base",max_new_tokens=20)
    text=image_to_text(url)[0]["generated_text"]
    print(text.capitalize())
    return text.capitalize()
img2text("photo2.jpg")
