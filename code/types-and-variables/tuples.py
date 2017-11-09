# Like lists, tuples can store a sequence of heterogeneously typed python objects. 
# Note that you use round brackets instead of square brackets to instantiate a tuple. 
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b = (13.2, 95.35, 2634.27, -0.251, 0.00152)
c = ('Hello', 'world')
d = (7, 42.4, -9, 36.75, 'g', 'Hello', 'World')

# In the same way as lists, elements of tuples can be accessed
b[1] # Gives 95.35

# We can also use len() to get the length of them
len(b) # Gives 5

# However, it's important to note that assignments and appends will result in an error
b[1] = 42 # Causes an error!
b.append(42) # Causes an error!