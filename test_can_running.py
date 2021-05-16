#! /usr/bin/env python3
# why just import urllib is error
# import urllib
import urllib.request
# why not urllib.error ,just use urllib is error
from urllib.error import URLError
# resolv question [SSL: CERTIFICATE_VERIFY_FAILED] 
# certificate verify failed: certificate has expired (_ssl.c:1056)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download(url):
    welcome = f"Downloading: {url}"
    print(welcome)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print(f"Download error:{e.reason}")
        html = None
    return html


website = 'https://www.kawabangga.com/posts/4249'
result = download(website)
if result:
    print(result.decode('utf8'))
