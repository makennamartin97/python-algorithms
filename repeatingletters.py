# Create a function that takes a string and returns a string in which each character is repeated once.

# double_char("String") ➞ "SSttrriinngg"

# double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"

# double_char("1234!_ ") ➞ "11223344!!__  "

def double_char(txt):
	res = ''
	for t in txt:
		res += t*2
	return res