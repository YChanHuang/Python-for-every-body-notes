#Assignment 9.4
#print('Hello World')

fname = input('Enter name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
handle = open(fname)

di = {} #create an empty dictionary
for line in handle:
    line = line.rstrip()
    wds = line.split()
    #the second for-loop to print each word in the list
    for w in wds :
        #if the key is not in the dictionar the count starts with 0
        ##oldcount = di.get(w,0)
        ##print(w, 'old', oldcount)

        ##newcount = oldcount + 1
        ##di[w] = newcount
        ##print(w, 'new', newcount)
        di[w] = di.get(w, 0) + 1
        #print(w, 'new', di[w])
        #workflow: retrieve/created/update counter
        #if w in di:
        #    di[w] = di[w] + 1
            #print('*Existing*') #To provide a hint of what the programmes is doing
    #    else:
    #        di[w] = 1
            #print('**New**') #To provide a hint of what the programmes is doing
#print(di)

#print the Most commoncommon word programme.
#mulitiple for-loop
largest = -1
theword = None
for k, v in di.items() : # times looks for the elements in dictionary
    print(k, v)
    if v > largest :
        largest = v
        theword = k # catch/remember the word that was largest
print('Most common', theword,largest)
