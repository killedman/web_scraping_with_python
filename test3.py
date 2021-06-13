"""
识别网站所用技术
"""
import builtwith
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

print(builtwith.parse('https://thinknotes.cn'))
print(builtwith.parse('http://ruanyifeng.com'))


"""
寻找网站所有者
我们可以使用WHOIS协议查看域名的注册者是谁。
Python中有一个针对该协议的封装库
其文档地址为https://pypi.python.org/pypi/python-whois，我们可以通过pip进行安装
python3 -m pip install python-whois
注意：测试发现whois无法查询到.cn的域名信息，可以通过站长工具的whois功能查询
"""
# import whois
# print(whois.whois('ruanyifeng.com'))
