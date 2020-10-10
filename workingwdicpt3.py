# have the function now return a summary dictionary such as this:

# { "managers": 2, "employees": 3, "owner": 2, "total_keys": 3, "total_values": 7 }

def dictionarySummary(list1):

    sum = 0
    for m in list1:
        list1[m] =len(list1[m])
        sum+=list1[m]
    list1["total_keys"] = len(list1)
    list1["total_values"] = sum

    return list1

staff = {
    "managers": [ "Michael", "John" ],
    "employees": [ "Howard", "Lori", "Elijah" ],
    "owner": [ "Bob", "Stuart" ] 
}