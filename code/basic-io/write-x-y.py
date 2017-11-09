# Code to write x and y coordinates.
x = [12, 23, 13, 12, 16]
y = [562, 762, 87, 97, 212]

# Opens the file for writing, creating it
# if it doesn't exist.
f = open('xydata.dat', 'w')

# Check that the file is open before we try to write
if f:
	# Iterate from 0 to length of the arrays minus 1
	# because the arrays are zero indexed.
	for i in range(0, len(x) - 1):
		f.write("{}\t{}\n".format(x[i], y[i]))

	# When we're done writing, we can close the file
	f.close()