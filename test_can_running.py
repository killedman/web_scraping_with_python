#! /usr/bin/env python3
# why just import urllib is error
# import urllib
from urllib.request import Request, urlopen  # Python 3
from urllib.error import HTTPError
# import urllib.request
# why not urllib.error ,just use urllib is error
from urllib.error import URLError
# resolv question [SSL: CERTIFICATE_VERIFY_FAILED] 
# certificate verify failed: certificate has expired (_ssl.c:1056)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def download(url, user_agent='wswp', num_retries=2):
    welcome = f"Downloading: {url}"
    print(welcome)
    req = Request(url)
    req.add_header('User-agent', user_agent)  # 修改Python默认的User-agent
    try:
        html = urlopen(req).read()  # urlopen(req).headers返回headers
    except HTTPError as e:
        print(f"Download error:{e.code, e.reason}")
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                print(e.code)
                # recursively retry 5xx HTTP errors
                return download(url, user_agent, num_retries-1)
    return html


website = 'https://www.kawabangga.com/posts/4249'
# website = 'http://httpstat.us/500'
result = download(website)
if result:
    # print(result.decode('utf8'))
    pass
