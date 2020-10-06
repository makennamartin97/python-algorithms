# Create a function that takes a string and returns the number (count) of 
# vowels contained within it.

# count_vowels("Celebration") ➞ 5

# count_vowels("Palm") ➞ 1

# count_vowels("Prediction") ➞ 4

def count_vowels(txt):
	count = 0
	reg = '/aeiou/'
	length = len(txt)
	for v in range(length):
		if txt[v] in reg:
			count = count + 1
	return count