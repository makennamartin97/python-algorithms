# Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.

# reverse(True) ➞ False

# reverse(False) ➞ True

# reverse(0) ➞ "boolean expected"

# reverse(None) ➞ "boolean expected"

def reverse(arg):
	if type(arg) != bool:
		return 'boolean expected'
	return not arg
		