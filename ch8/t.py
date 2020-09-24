fh = open('mbox-short.txt')
count = 0

for line in fh:
    if not line.startswith('From'):
        continue
    line = line.rstrip()
    word = line.split()
    count = count + 1
    print(line)
