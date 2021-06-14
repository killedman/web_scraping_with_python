#! /usr/bin/env python3
from urllib.request import urlopen
from urllib.error import URLError


def download(url):
    welcome = f"Downloading: {url}"
    print(welcome)
    try:
        html = urlopen(url).read()
    except URLError as e:
        print(f"Download error:{e.reason}")
        html = None
    return html


website = 'http://www.ruanyifeng.com/home.html'
result = download(website)
if result:
    print(result)
