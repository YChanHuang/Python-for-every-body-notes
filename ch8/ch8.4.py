#solution 1
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	words = line.split()
	for word in words:
		if word in lst:
			continue
		else:
			lst.append(word)
lst.sort()
print(lst)

#solution 2
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
