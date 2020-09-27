name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


di = {}
hours = {}
for line in handle:
    if line.startswith('From '): #I forgot the space while the first trial
        line = line.rstrip()
        words = line.split()
        tm = [] # create an empty list
        tm = words[5].split(":") # time is at position"6"
        # print(tm[0])
        hours[tm[0]] = hours.get(tm[0], 0) +1 # create a key, value dict
# print(hours)

tmp = list()
for k, v in hours.items():
    tpl = (k, v)
    # print(tpl)
    tmp.append(tpl)
# print(tmp)
tmp = sorted(tmp)
# print(tmp)
for k, v in tmp:
    print(k,v)
