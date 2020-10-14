# leetcode rotate array

def rotate(nums, k):
    # assign variable to last index
        last = len(nums)-1
    # loop through k times
        for i in range(k):
    # move last val to the front and remove
            nums.insert(0, nums[last])
            nums.pop()
        return nums
print(rotate([1,2,3,4,5,6,7], 3))