"""
通过id遍历下载；
设置最大错误数，解决中间id被删除导致的提前终止
"""
import itertools
from crawl_sitemap import download


# maximum number of consecutive download errors allowed
max_errors = 5
# current number of consecutive download errors
num_errors = 0
for page in itertools.count(1):
    url = 'http://127.0.0.1:8000/places/default/view/%d' % page
    # print(url)
    html = download(url)
    if html is None:
        # received an error trying to download this webpage
        num_errors += 1
        if num_errors == max_errors:
            # reached maximum number of
            # consecutive errors so exit
            break
    else:
        # success - can scape the result
        num_errors = 0
