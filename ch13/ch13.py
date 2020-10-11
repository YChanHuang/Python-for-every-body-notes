import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# holder for url
url ='http://py4e-data.dr-chuck.net/comments_874986.xml'
html = urllib.request.urlopen(url, context = ctx)
data = html.read() # open and read the data

tree = ET.fromstring(data) # transfrom the data into string
lst = tree.findall('comments/comment') # locate to the position of comment

# for i in lst:
    # print(i)
## method 1
sum = 0
for item in lst:
    sum += int(item.find('count').text) # locate to count and find text
    print(sum)
# counts = tree.findall('.//count')
# sum = 0
# for count in counts:
#     sum = sum + int(count.text)
# print(sum)
#
