## Ch13- Objects oriented
![image1](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20201014122956.png?token=AJ7JITHD6D6WHE3DHO5OF4K7Q3QXC)

![image2](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20201014150630.png?token=AJ7JITGVM6TZSNHELU4GAGS7Q4DCQ)

### Key elements
1. Class | Attribute
2. Objects | instance
3. Basic syntax:
(1) Build Class: `class Point:`
(2) Define initial fuction:`def __init__(self):`
(3)

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = Point(3, 4)
print(p1.x, p1.y)

p2 = Point(5, 6)
print(p2.x, p2.y)
```

## SQLite

1. (128) is the contractor to decide the data size.
![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20201014180143.png?token=AJ7JITGHTSYUO3YJGEW5Y4S7Q4XTK)

2. 



- Ojbect is like a cookie
- Class
- No numbers in the beginning
- Captial letter

- Basic example `Class.Attribute()`
- Full sample
```
Class IO:
  supportedSrcs = ['console', 'file']
  def read(src):
      print('Read from:', src)
```
