# merge sort
# Merge sort first divides the array into equal halves and then combines 
# them in a sorted manner.
unsortedlist = [64, 34, 25, 12, 22, 11, 90]
def mergesort(unsortedlist):
    if len(unsortedlist) <= 1:
        return unsortedlist
    # find middle pt and divide it
    mid = len(unsortedlist) //2
    leftlist = unsortedlist[:mid]
    rightlist = unsortedlist[mid:]

    leftlist = mergesort(leftlist)
    rightlist = mergesort(rightlist)
    return list(merge(leftlist,rightlist))

# Merge the sorted halves
def merge(left,right):
    res = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            res.append(left[0])
            left.remove(left[0])
        else:
            res.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        res = res + right
    else:
        res = res + left
    
    return res

print(mergesort(unsortedlist))

