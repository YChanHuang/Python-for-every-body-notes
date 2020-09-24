#Assignment 8.5
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = []
for line in fh:
    line = line.rstrip()
    word = line.split()
    lst.append(word)
print(lst)
#print("There were", count, "lines in the file with From as the first word")
