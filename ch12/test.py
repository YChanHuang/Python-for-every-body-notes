### code2
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re


repeat = 7
pos = 18
url = 'http://py4e-data.dr-chuck.net/known_by_Setana.html'
for n in range(repeat):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')
    URL = tag[pos - 1].get('href', None)
    print(URL)


###Code 2
import urllib.request
from bs4 import BeautifulSoup

lp = 18
#times the process is repeated
#tpr = 4
tpr = 7
# url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Setana.html'
for i in range(tpr):
    url = BeautifulSoup(urllib.request.urlopen(url).read())('a')[lp - 1].get('href', None)
    print(url)
