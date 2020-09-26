name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di = {}
for line in handle:
    if line.startswith('From '): #I forgot the space while the first trial
        line = line.rstrip()
        words = line.split()
        email = list()
        # it should use list to store the email otherwise the loop would treat extracted data as a massive string
        email.append(words[1])
        for em in email:
            di[em] = di.get(em, 0) + 1
        # print(di)
largest = -1
prolific_em = None
for k,v in di.items():
    if v > largest :
        largest = v
        prolific_em = k
print(prolific_em, largest)
