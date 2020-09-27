import re
fh = open('actual.txt')

sum = 0 # create a starting point

for line in fh:
    nums = re.findall('[0-9]+', line)
    if len(nums) < 1 : continue 
    # print(nums)
    for n in nums :
        sum = sum + int(n) # change the number into interger
print(sum)
