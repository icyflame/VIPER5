inFile = open('viper','r')

out = open('newFile','w')

import string

for i in inFile:	

	i = str(i)

	if not i[8] == ':':
	
		out.write('username' + ':' + i[8:])	##the '\n' is present at the end! and as the colon is not there
							## we have to start from the 8th location of the base string.
		
	else:
	
		out.write(i)	

out.close()
inFile.close()

inFile = open('newFile','r')

for i in inFile:

	print i
