fhand = raw_input("file name ? ")
fh = open(fhand)
z = list()
for line in fh:
    x = line.split()
    for i in x:
        if i in z:
            continue
        else :
            z.append(i)
z.sort()
print z





#fname = raw_input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#	line = line.rstrip()
#	word = line.split()
#	for element in word :
#		if element in lst:
#			continue 
#		lst.append(element)
#lst.sort()
#print lst
    
    
