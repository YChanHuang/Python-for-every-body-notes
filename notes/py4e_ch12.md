# Ch 12 Access web data in Python
## key points

- TCPIP
- port

## 12.1 Socket library in Python


1. Connect to the website
 `import socket`



![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20200927124202.png?token=AJ7JITEDJSI7M77MXMU4KCK7OB5MO)

## 12.2
- HTTP (Hypertext Transfer Protocol)

- It allows the browser to retrieve the document from the Internet.
![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20200927125134.png?token=AJ7JITF3AQ2U7BZNNVSWWTC7OB6QG)

- Request / response cycle.
![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20200927125414.png?token=AJ7JITDVGJABXDOSXR32C3S7OB62I)

- Get
![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20200927125652.png?token=AJ7JITANP4M4PKR5RQ2Y5TK7OB7EC)

### Telnet (Mac OS / Linux)

``telnet data.pr4e.org 80``

## HTTP Request in Python (Pseudo code)
1. Setting up the socket
2. Sending the request
3. Preparing to receive the metadata
4. Receiving data
5. Intepreting ``decode()``

```
import Socket
mysock = socket.socket(net, stream)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET domain.encode()'
mysock.send(cmd)

While True:
  data = mysock.recv(512)
  if (len(data) < 1):
    break
  print(data.decode())
mysock.close()
```

## Encode & decode


# String
## ASCII
`ord()` tells the numerical value of character

```
print(ord('H'))
72
```
## Unicode
- **UTF-8** : 1-4 bytes
- In Python3 all **strings are Unicode**
- In Python3, string and Unicode string are the same, but is different from

```
...
cmd = "GET ....encode()" # encode the string into bytes


While True:
  data = mysock.recv(512) #bytes
  if (len(data) < 1):
    break
    mystring = data.edcode() # this is string in UTF8
    print(mystring)
```

![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20200928115951.png?token=AJ7JITC5OVRSLVBLSB55VXS7OHBGI)


## ch12.3
### urllib in Python3

![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20200928120442.png?token=AJ7JITBGIZQ3M6FDDGT3J3K7OHBYO)

```
import urllib.request, urllib.parse, urllib.error

fhand = url lib.request.urlopen('URL')
#this opens URL and store it as file

for line in fhand:
  print(line.decode().strip())

```


- Readable formats: **htm**, **txt**
(html is normally behind **'href='**)


## BeautifulSoup library
- Searching the strings effectively and quickly








**All the screenshots are credited to the University of Michican**
