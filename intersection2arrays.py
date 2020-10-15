# leetcode intersection of 2 arrays
# Given two arrays, write a function to compute their intersection.

def intersect(nums1, nums2):
    # create new array
    res = []
    # iterate through array 1
    for i in nums1:
        # if i is in array 2 as well, add to result and remove from og array
        if i in nums2:
            res.append(i)
            nums2.remove(i)
    return res

# testing

print(intersect([4,9,5], [9,4,9,8,4])) # [4, 9]
print(intersect([1,2,2,1], [2,2])) # [2, 2]
