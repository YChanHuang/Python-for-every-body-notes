name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = {}
for line in handle:
    if line.startswith('From '): #I forgot the space while the first trial
        line = line.rstrip()
        words = line.split()
        email = []
        email.append(words[1])
        for em in email:
            di[em] = di.get(em, 0) + 1
#print(di)

# x = sorted(di.items())

# construct a test_list
tmp = list()
for k,v in di.items():
    newtpl = (v, k)
    tmp.append(newtpl)

#print('Flipped' ,tmp)
tmp = sorted(tmp, reverse = True)
# print('Sorted', tmp[:5])
#flip the tuples in a list
for v,k in tmp[:5]:
        print(k, v)
