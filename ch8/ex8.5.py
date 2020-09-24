#Assignment 8.5
#file name = mbox-short.txt
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): #To check if the line staty with 'From '
            continue    #Note that there is a space behind the From, otherwise the print resuly would duplicated
    word = line.split()
    count = count + 1
    print(word[1]) #

print("There were", count, "lines in the file with From as the first word")
