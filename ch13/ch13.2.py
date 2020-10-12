# load the require librarioes 
import json
import urllib.request, urllib.error, urllib.parse

url = 'http://py4e-data.dr-chuck.net/comments_874987.json'
uh = urllib.request.urlopen(url)

data = uh.read().decode() #decode url into js
# print(data)

#read json file
js = json.loads(data)
# print(json.dumps(js, indent = 2))
sum = 0
for n in js['comments']:
    sum += int(n['count'])
print(sum)
