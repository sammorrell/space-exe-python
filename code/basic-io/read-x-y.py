# Code to read x and y coordinates

filename = 'xydata.dat'
x = []
y = []

# First we open the file
f = open(filename, 'r')

# We can read the entire contents of the file into
# a string, like so
entire_file = f.read()

# Or we can read each line into an element in a list.
# Before that, we seek the start of the file to read it in again. 
f.seek(0, 0)
rows_of_file = f.readlines()

# We can loop over the lines in a file like so
for row in rows_of_file:
	tmp = row.replace('\n', '')
	x_tmp, y_tmp = tmp.split(" ")
	x.append(float(x_tmp))
	y.append(float(y_tmp))

# Finally we close the file
f.close()

print(x) # [12.0, 23.0, 13.0, 12.0, 16.0]
print(y) # [562.0, 762.0, 87.0, 97.0, 212.0]