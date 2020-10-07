# Luke Skywalker has family and friends. Help him remind them who is who. 
# Given a string with a name, return the relation of that person to Luke.

# relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

# relation_to_luke("Leia") ➞ "Luke, I am your sister."

# relation_to_luke("Han") ➞ "Luke, I am your brother in law."

def relation_to_luke(name):
	dic = {"Darth Vader":"father","Leia":"sister","Han": "brother in law",
	"R2D2":"droid"}
	for key, value in dic.items():
		if name == key:
			return "Luke, I am your " + value + "."