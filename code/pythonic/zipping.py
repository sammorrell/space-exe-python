# Zip combines the two or more arrys into a single 
# for loop, leting you easily iterate over the values

list1 = ['a1', 'a2', 'a3', 'a4', 'a5']
list2 = ['b1', 'b2', 'b3', 'b4', 'b5']

for l1, l2 in zip(list1, list2):
	print('{}, {}'.format(l1, l2))

# Will print:
# a1, b1
# a2, b2
# a3, b3
# a4, b4
# a5, b5

