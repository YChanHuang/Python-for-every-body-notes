
import sqlite3
# import urllib.request, urllib.parse

conn = sqlite3.connect('orgdb.sqlite') # connet to the database
cur = conn.cursor() # this is similar to handler



cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#Indicating the file (URL in this case) from where we'll read the data
# fname = "http://www.pythonlearn.com/code/mbox.txt"
fname = 'mbox.txt'
fh = open(fname)


for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    orgs = pieces[1]
    org = orgs.split('@')[1]


    cur.execute('SELECT count FROM counts WHERE org = ?',
                (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1) ''', (org, ))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org, ))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
