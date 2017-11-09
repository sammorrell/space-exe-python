# You can get a value from the console like this
name = input('What is your name?: ') # What is your name?: Sam

# You can chain this together with .format() and type
# conversions to make your program really interactive
age = int(input('Hello, {}. How old are you?: '.format(name))) 

# Inputting a true or false here will convert it to a bool
member = bool(input('Are you a member of Space Exe, {}?: '.format(name))) # True