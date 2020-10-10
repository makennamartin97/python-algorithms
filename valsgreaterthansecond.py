# Objectives
# Write a function that accepts a list and creates a new list containing only 
# the values from the original list that are greater than its 2nd value. Print 
# how many values this is and then return the new list. If the list has less 
# than 2 elements, have the function return False.

# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return 
# [5, 3, 4]
# Example: values_greater_than_second([3]) should return False

def values_greater_than_second(list1):
    new = []
    count = 0

    x = list1[1]
    for i in list1:
        if i > x:
            new.append(i)
            count+=1
    print(count)
    return new

# testing
print(values_greater_than_second([5,2,3,2,1,4,7,15,-3]))
