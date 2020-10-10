# create a function that takes a dictionary such as above, and returns a new 
# dictionary that looks like below:
# { "managers": 2, "employees": 3, "owner": 2 }

def dictionarySummary(list1):
    for m in list1:
        list1[m] =len(list1[m])

    return list1

staff = {
    "managers": [ "Michael", "John" ],
    "employees": [ "Howard", "Lori", "Elijah" ],
    "owner": [ "Bob", "Stuart" ] 
}