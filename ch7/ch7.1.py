#exercise

#read the text file

fname = input('enter your file name')
fh = open(fname)

for lines in fh:
    lines = lines.rstrip()
    print(lines.upper())
