import random
import string
s = "rock , paper or scissor game "
print s.upper()
print ' choose r for rock \n choose p for paper  \n choose s for scissor '
cpoint = 0
upoint = 0
print "rock , paper or scissor(r/p/s)  "

for i in range (1,6):
    cchoice = random.randint(1,3)
    if cchoice == 1:
        cchoice = 'r'
    elif cchoice == 2:
        cchoice = 'p'
    else:
        cchoice = 's'
    uchoice = raw_input("enter your option : ")
    uchoice = uchoice.lower()
    print "computer choice " , cchoice 
    if uchoice == cchoice:
        print "ITS A TIE"
    elif (uchoice == 'r' and cchoice == 's') or (uchoice == 'p' and cchoice == 'r') or (uchoice == 's' and cchoice == 'p'):
        print " user wins a point"
        upoint += 1
        print "user point " , upoint
        print "computer point " , cpoint
    elif (uchoice == 'r' and cchoice == 'p') or (uchoice == 'p' and cchoice == 's') or (uchoice == 's' and cchoice == 'r'):
        print " computer wins a point"
        cpoint += 1
        print "user point " , upoint
        print "computer point " , cpoint
if cpoint > upoint:
    x = cpoint - upoint 
    print " \n \n computer won by " , x ,"points"
elif upoint > cpoint:
    x = upoint - cpoint
    print "\n \n user won by " , x ,"points"
else:
    print "\n \n its a tie"
    
