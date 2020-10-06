# *in python instead of slice use a[1:4] format

# Create a function that takes date in the format yyyy/mm/dd as an input and 
# returns "Bonfire toffee" if the date is October 31, else return "toffee".

# halloween("2013/10/31") ➞ "Bonfire toffee"

# halloween("2012/07/31") ➞ "toffee"

# halloween("2011/10/12") ➞ "toffee"

def halloween(dt):
	x = dt[5:10]
	if x == "10/31":
		return "Bonfire toffee"
	else:
		return "toffee"