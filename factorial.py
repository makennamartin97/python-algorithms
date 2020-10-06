# Create a function that takes an integer and returns the factorial of that 
# integer. That is, the integer multiplied by all positive lower integers.

# factorial(3) ➞ 6

# factorial(5) ➞ 120

# factorial(13) ➞ 6227020800

def factorial(num):
	if num < 2:
		return num
	else:
		return factorial(num-1) * num