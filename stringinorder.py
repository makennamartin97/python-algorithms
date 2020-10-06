# Create a function that takes a string and returns True or False, depending on whether the characters are in order or not.

# is_in_order("abc") ➞ True

# is_in_order("edabit") ➞ False

# is_in_order("123") ➞ True

# is_in_order("xyzz") ➞ True

# is_in_order("abc") ➞ True

# is_in_order("edabit") ➞ False

# is_in_order("123") ➞ True

# is_in_order("xyzz") ➞ True

def is_in_order(txt):
	return list(txt) == sorted(txt)