
def pedantic_square_root(number):
	from math import sqrt
	root = sqrt(number)
	return (root, -root)

# We can give only one variable to assigne and 
# we just get the tuple returned
root = pedantic_square_root(4) 
print('{}'.format(root)) # (2.0, -2.0)

# However, because the function returns a tuple
# we can unpack them into two variables
root1, root2 = pedantic_square_root(4) 
print('{} {}'.format(root1, root2)) # 2.0 -2.0