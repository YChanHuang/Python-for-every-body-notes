name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = {}
for line in handle:
    if line.startswith('From '): #I forgot the space while the first trial
        line = line.rstrip()
        words = line.split()
        email = words[2]
        # print(email)
        for em in words:
            di[em] = di.get(em, 0) + 1
        print(di)

# prolific_em = None
# largest = -1
# for v,k in di:
#     if v > largest :
#         largest = v
#         prolific_em = k
# print(prolific_em, largest)
#
#
#
#         print(words)
