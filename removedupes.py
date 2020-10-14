# leetcode remove dupes in python



def removeDuplicates(nums):
    # check to see if there is only one val
        if len(nums) <= 1:
            print(nums)
            return len(nums)
        else:
        # assign index var to iterate backwards
            i = len(nums)-1
            while i > 0:
                # check the prev val and remove if dupe
                prev = nums[i-1]
                if (nums[i] == prev):
                    nums.remove(nums[i])
                i = i-1
                
            print(nums)
            # get the updated length and return
            length = len(nums)
            return length

# testing

print(removeDuplicates([1,1,2,3,3,3,4,4,5,6,6]))
# [1, 2, 3, 4, 5, 6]
# 6
print(removeDuplicates([1,1]))
# [1]
# 1
print(removeDuplicates([1,1,2,2,2,3,4,4,5,5,]))
# [1, 2, 3, 4, 5]
# 5