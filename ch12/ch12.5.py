# load in the required packages for reading HTML

from urllib.request import urlopen
from bs4 import BeautifulSoup #parser for HTML
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#open the url
url = 'http://py4e-data.dr-chuck.net/comments_874984.html'
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrive the information form url
spans = soup('span')
sum = 0
for span in spans:
    x = span.contents[0]
    for n in x:
        sum = sum + int(n)
print(sum)


sum=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    y=str(tag)
    x= re.findall("[0-9]+",y)
    for i in x:
        i=int(i)
        sum=sum+i
print(sum)

#
