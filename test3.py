"""
识别网站所用技术
"""
import builtwith
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

print(builtwith.parse('https://thinknotes.cn'))
print(builtwith.parse('http://ruanyifeng.com'))
