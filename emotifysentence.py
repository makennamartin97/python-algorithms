# Create a function that changes specific words into emoticons. 
# Given a sentence as a string, replace the words smile, grin, 
# sad and mad with their corresponding emoticons.

# emotify("Make me smile") ➞ "Make me :D"

# emotify("Make me grin") ➞ "Make me :)"

# emotify("Make me sad") ➞ "Make me :("

def emotify(txt):
	face = {
		'smile': ':D', 'grin': ':)', 'sad': ':(', 'mad':':P'
		
	}
	for f in face.keys():
		if f in txt:
			txt = txt.replace(f, face[f])
	return txt