# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ") # allow user to type the file name
try:
    fh = open(fname)
except:
    print("File does not exist")
    quit() #when the file does not exist, then stop the programme
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    num_start = line.find(' ') 
    num_strip = line[num_start+1:].strip()
    num_float = float(num_strip)
    count = count + 1
    total = total + float(num_float)
AVG = total / count

print('Average spam confidence: ', AVG)
