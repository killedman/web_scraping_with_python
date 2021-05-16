#! /usr/bin/env python3
import urllib


def download(url):
    welcome = f"Downloading: {url}"
    print(welcome)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print(f"Download error:{e.reason}")
        html = None
    return html


website = 'http://www.ruanyifeng.com/home.html'
result = download(website)
if result:
    print(result)
