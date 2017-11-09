# A demonstration of how to use keyworded arguments within your functions. 

def greeter(name, **kwargs):
	greeting = kwargs['greeting'] if 'greeting' in kwargs else 'Hello, '
	ending = kwargs['ending'] if 'ending' in kwargs else '. '
	print('{}{}{}'.format(greeting, name, ending))

# First we can call it without a keyword argument
greeter('World') # Hello, World. 
greeter('World', greeting='Howdy, ') # Howdy, World. 
greeter('World', ending='! ') # Hello, World! 
greeter('World', greeting='Sup, ', ending='? ') # Sup, World?