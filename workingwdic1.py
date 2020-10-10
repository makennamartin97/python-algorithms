# Given this dictionary, how would you write a function to print each value 
# in this exact format?

# managers
# - Michael
# - John
# employees
# - Howard
# - Lori
# - Elijah
# owner
# - Bob
# - Stuart
staff = {
    "managers": [ "Michael", "John" ],
    "employees": [ "Howard", "Lori", "Elijah" ],
    "owner": [ "Bob", "Stuart" ], 
}

def printStaffInfo(staff):

    for s in staff:
        print(s)
    for o in staff[s]:
        print("- " + o)