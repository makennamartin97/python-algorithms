# Objectives
# Given a list of numbers, create a function to replace the last value with 
# the number of positive values. Note that zero is not considered to be a 
# positive number.

# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3]
# and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] 
# and returns it

def count_positives(list1):
    count = 0
    l = len(list1)
    for i in range(l):
        if list1[i] > 0:
            count+=1
            list1[l-1] = count
    return list1

# testing
print(count_positives([-5,-3,0,3,5]))