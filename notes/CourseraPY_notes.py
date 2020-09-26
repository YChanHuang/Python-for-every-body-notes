# learn python notes

# Loop in python
#    "While" is the keyword

while n > 4
    funtion
    n = n - 1
print("hi")


# For loop
for i in []
    print()


zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)
##
#
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break

    try :
	    fnum = float(num)
    except :
        print('Invalid input')
        continue

	if ((smallest is None) or (fnum < smallest)):
	    smallest = int(fnum)
	if ((largest is None) or (fnum > largest)):
	    largest = int(fnum)

print("Maximum is ", largest)
print("Minimum is ", smallest)


####
# Initialising variables
smallest = None
largest = None

# Starting loop
while True:
    # Ask for the user input
    sval = input('Enter a number: ')

    # If user types 'done' then exit
    if sval == 'done': break

    # Trying to convert user input to a value, but if it is not working, give an error message
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue

    # Adjusting counters
    if ((smallest is None) or (fval < smallest)):
        smallest = int(fval)
    if ((largest is None) or (fval > largest)):
        largest = int(fval)

# Printing the total, the number of inputs and the average
print('Maximum is', largest)
print('Minimum is', smallest)



largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == "done" :
        break

    try :
	    fnum = float(num)
    except :
        print('Invalid input')
        continue

    if smallest is None:
        smallest = fnum
	elif num < smallest:
        smallest = fnum


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
	    n = int(num)
    except :
        print('Invalid input')
        continue

	if smallest is None:
		smallest = n
	elif n < smallest:
		smallest = n
	elif largest is None:
        largest = n
	elif largest > n:
        lergest = n

print("Maximum", smallest)

x = '40'
y = int(x) + 2
print(y)
