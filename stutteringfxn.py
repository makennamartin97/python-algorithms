# Write a function that stutters a word as if someone is struggling to read it. 
# The first two letters are repeated twice with an ellipsis ... and space after 
# each, and then the word is pronounced with a question mark ?.

# stutter("incredible") ➞ "in... in... incredible?"

# stutter("enthusiastic") ➞ "en... en... enthusiastic?"

# stutter("outstanding") ➞ "ou... ou... outstanding?"

def stutter(word):
	new = word[0] + word[1] + '... '
	return new + new + word + '?'

print stutter('makenna')
