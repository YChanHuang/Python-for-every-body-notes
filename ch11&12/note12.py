import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# encode() is to convert unicode to UTF-8
# since the string in Python is
mysock.send(cmd)

while True:
    data = mysock.recv(512) #receive up to 512 character
    if len(data) < 1: # if the data is less than 1 than quit the programme
        break
    print(data.decode(),end='')

mysock.close() #close the socket connection

# Code: http://www.py4e.com/code3/socket1.py
