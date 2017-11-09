# We can generate a new array using a generator, like the range function
array1 = [ x + 1 for x in range(10)  ] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# We can generate a new list from the values of a previous list
array2 = [ i * 10 for i in array1 ] # [10, 20, 30, 40, 50, 60 70, 80, 90, 100]

# We can add in the conditional clause to filter off certain values
array3 = [ x for  x in array1 if x % 2 == 0 ] # [2, 4, 6, 8, 10]