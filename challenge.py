
# print out the integer numbers from 30 to 300 

listofnumber = range(30,301)
for i in listofnumber:
	if (i%7 == 0 and i%13 == 0 ):
		print "a-z", i
	else:
		if (i%7 == 0):
			print "abc", i
		if (i%13 == 0):
			print "xyz", i
