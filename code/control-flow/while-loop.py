# In this example we have an unknown integer and the user to guess what it is.
# We're going to make it easier and tell them whether it's higher or lower.
number = 42
guess = 0

while number != guess:
	guess = int(input('Guess the integer: '))

	if number == guess:
		print("Well done, you got the number!")
	elif number > guess:
		print('Sorry, your guess was incorrect. The number is higher. Try again.')
	else:
		print('Sorry, your guess was incorrect. The number is lower. Try again.')