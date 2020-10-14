# leetcode contains duplicate in python

def containsDuplicate(nums):
    # sort the array so dupes are in order
    nums.sort()
    # find last index
    last = len(nums)-1
    # set bool to false
    isTrue = False
    # iterate through and if there is a dupe, the boolean will change to True
    for i in range(last):
        if nums[i] == nums[i+1]:
            isTrue = True
    # return isTrue whether dupe found or not
    return isTrue
            