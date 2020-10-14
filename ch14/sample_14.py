## database and Python
# import the library

import sqlite3
conn = sqlite3.connect('emaildb.sqlite') # connet to the database
cur = conn.cursor() # this is similar to handler

#Excute the lines to delete the TABLE
cur.excute(```
DROP TABLE IF EXISTS Counts```
)

#Create the lines to delete the TABLE
cur.excute(```
           CREATE TABLE Counts (email TEXT, count INTEGER)```)
#
fname = "file.name"
# if (len(fname) < 1): fname

fh = open(fname)


cur.commit()

cur.close()
