# We can make simple decisions and assignments much easier using this construct
a = 10
print('Hello, World') if a == 10 else None # Hello, World
c = True if a > 5 else False # a = True

# You can combine it with the 'in' to see if something is in an array or dictionary. 
committee  = ['Ben', 'Marine', 'Mark', 'Matt', 'Sam']
name = 'Jim'
print('On committee') if name in committee else print('Not on committee')
# Not on committee