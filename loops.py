largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	if num == "done":
		break
	try:
		num = int(num)
	except:	
		print "Invalid input"
		continue	
	if smallest is None :
		smallest = num
	if num > largest:
		largest = num
	if num < smallest:
		smallest = n
print "Maximum is",largest
print "Minimum is",smallest
