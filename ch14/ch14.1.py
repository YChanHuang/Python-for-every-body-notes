
import sqlite3
conn = sqlite3.connect('emaildb.sqlite') # connet to the database
cur = conn.cursor() # this is similar to handler

cur.excute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = 'mbox.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: '):continue
    pieces = line.split()
    print(pieces)
    # email = pieces[1]
