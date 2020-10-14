# import the libraries
import urllib.request, urllib.parse, urllib.error, urllib
import json
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


#url and place
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
address = 'University College Dublin'

parameter = ({'key': 42,'sensor':'false', 'address': address})

url = serviceurl + urllib.parse.urlencode(parameter)
# print(url)
uh = urllib.request.urlopen(url) # open the url
# print(uh)
data = uh.read().decode()
print(data)
js = json.loads(data)
# print(json.dumps(js, indent = 2))
print(js['results'][0]['place_id'])




#
import json
import urllib.request, urllib.error, urllib.parse

#Stroring the given parameters
serviceurl = "http://python-data.dr-chuck.net/geojson?"
sample_address = "South Federal University"
data_address = 'University College Dublin'
address_wanted = data_address

#Setting the GET parameters on the URL
parameters = {"sensor": "false", "address": address_wanted}
paramsurl = urllib.parse.urlencode(parameters)

#Generating the complete URL. Printing it in order to check if it's correct.
queryurl = serviceurl + paramsurl
print("DATA URL: ", queryurl)

#Obtaining and reading the data
data = urllib.request.urlopen(queryurl).read().decode()

#Parsing the data and looking for the field we want.
#That field is inside the "Results" array, in its first item (if our address is
#correct we can assume that the result would be the correct one) and on its
#"place_id" field
jsondata = json.loads(data)
place_id = jsondata["results"][0]["place_id"]
print("PLACE ID: ", place_id)
