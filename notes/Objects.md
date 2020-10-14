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


---
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
### Create a table
```
CREATE TABLE users(
	name VARCHAR(128),
	email VARCHAR(128)
)
```

- (128) is the contractor to decide the data size.
![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20201014180143.png?token=AJ7JITGHTSYUO3YJGEW5Y4S7Q4XTK)

### Insert data to database
``INSERT INTO users(name, email) VALUES('Kris', 'kris37@ac.uk')``
- `INSERT INTO ... VALUES`

### Delete data
``DELETE FROM users WHERE email = 'kris37@ac.uk' ``
- Where is that condition.
- `DELETE FROM`
- `DELETE ... SET`

### Update

`UPDATE users SET name = 'Kris' WHERE email = 'kris737@lc.ac.uk'`

### SELECT
- Select all the data from the table.
`SELECT * FROM users`

![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20201014181448.png?token=AJ7JITFCNQXT6WJXCMKP5AC7Q4ZEK)

`SELECT * FROM users WHERE name = 'Kris'`

![](https://raw.githubusercontent.com/YChanHuang/UploadedPic/master/20201014181527.png?token=AJ7JITHZFZBCP7H4NT5B4QK7Q4ZGW)
