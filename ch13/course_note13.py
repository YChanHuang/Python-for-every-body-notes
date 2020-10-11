# hot to pull out data from xml
# import the xml library
imort xml.etree.ElementTree as ET

# data = ...
# ...

tree = ET.fromstring(data) # retrive the data from xml as a tree by ET library

print('Name', tree.find('name').text)  # To find the tag name
print("Attr", tree.find('email').get('hide')) # get the tag under email
