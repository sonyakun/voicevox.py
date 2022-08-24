import requests
import urllib
import urllib.request
from asyncio import run, gather

def vbox_web():
    global apiKey,text,vbox_file_name
    post = requests.get(f"https://api.su-shiki.com/v2/voicevox/audio/?key={apiKey}&speaker=0&pitch=0&intonationScale=1&speed=1&text={text}")
    with open(vbox_file_name, "wb") as fp:
        fp.write(post.content)