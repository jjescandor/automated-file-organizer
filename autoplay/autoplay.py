from dotenv import load_dotenv
from selenium import webdriver
from urllib.request import Request, urlopen

req = Request('http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

import os
import time
import urllib, json
import ssl
import requests


ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
YOUTUBE_CHANNEL = os.getenv("YOUTUBE_CHANNEL")

def look_for_new_video():
    api_key = GOOGLE_API_KEY
    channel_id = YOUTUBE_CHANNEL
    base_video_url = "https://www.youtube.com/watch?v="
    base_search_url = "https://youtube.googleapis.com/youtube/v3/search?"
    print("Hi 1")
    

    url = base_search_url + 'part=snippet&channelId={}&maxResults=1&order=date&key={}'.format(channel_id, api_key)
    inp = urlopen(url)
    print("hey", inp)
    resp = json.load(inp)
    print("Hi 2")

    vidID = resp['items'][0]['id']['videoId']

    with open('videoid.json', "r") as json_file:
        data = json.load(json_file)
        print("Hi 3")
        if data['videoId'] != vidID:
            driver = webdriver.Firefox()
            driver.get(base_video_url + vidID)
            video_exists = True
    
    if video_exists:
        with open('videoid.json', 'w') as json_file:
            data = {'videoId' : vidID}
            json.dump(data, json_file)

try:
    while True:
        print("Hi 0")
        look_for_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print('stooping')