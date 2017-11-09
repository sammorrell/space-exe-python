# Lists are capable of storing a load of different types. 
# For example, integers, floats, strings and a combination thereof. 
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [13.2, 95.35, 2634.27, -0.251, 0.00152]
c = ['Hello', 'world']
d = [7, 42.4, -9, 36.75, 'g', 'Hello', 'World']

# Elements within a list can be accessed and assigned simply using square brackets.
a[5] = 23
b[3] # Outputs: -0.251

# Something that can be really useful is the ability to append things to your lists
a.append(10) # Now a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# At any point you can find the number of elements inside the list using the len() function.
len([0, 1, 2, 3, 4]) # In this case, len() gives you 5.