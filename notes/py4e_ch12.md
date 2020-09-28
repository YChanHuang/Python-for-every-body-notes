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
