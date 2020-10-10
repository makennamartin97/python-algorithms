# Objectives
# Create a function that takes a list and returns a dictionary that has the 
# sumTotal, average, minimum, maximum, and length of the list.

# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 
# 'average': 7.75, 'minimum': -9. 'maximum': 37, 'length': 4 }

def ultimate_analysis(list1):
    sum = 0
    min = list1[0]
    max = list1[0]
    for i in list1:
        sum+=i
        if i < min:
            min = i
        if i > max:
            max = i
    avg = sum / len(list1)
    result = {"sumTotal": sum, "average": avg, "minimum": min, "maximum": max, "length": len(list1)}
    return result