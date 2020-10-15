# leetcode twosum

def twoSum(nums, target):
    # get length of nums and iterate
        l = len(nums)
        for i in range(l):
            # assign the value of the starting index to val
            # and find the diff between the target and val, so we know 
            # what to look for
            val = nums[i]
            sub = target - val
            # if the both the val and the diff are in the array, and the index
            # is not the same as the diff's index, return
            if sub in nums and nums.index(sub) != i:
                return [i, nums.index(sub)]

# testing
print(twoSum([5,9,4,8,2,1], 10)) # [1, 5]
print(twoSum([3,3],6)) # [1,0]

