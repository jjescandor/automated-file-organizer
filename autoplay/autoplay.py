from dotenv import load_dotenv
from selenium import webdriver

import os
import time
import urllib, json

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def look_for_new_video():
    api_key = GOOGLE_API_KEY
    print(api_key)