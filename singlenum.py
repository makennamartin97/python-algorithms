# leetcode single number

def singleNumber(nums):
    # create dictionary 
    subdict = dict()
    # iterate thru nums and add to the dict, assigning each val to 0
    # initially and adding 1 to the val every time the key is already present
    for n in nums:
        subdict[n] = subdict.get(n, 0) +1
    # iterate thru the dict and if theres a val less than 2, return the key
    for k, v in subdict.items():
        if v < 2:
            return k
    return 'No single nums present'


# testing
print(singleNumber([4,1,2,1,2])) # 4
print(singleNumber([3,9,2,0,9,3,2])) # 0
print(singleNumber([4])) # 4
print(singleNumber([])) # No single nums present
print(singleNumber([2,7,2,9,7,9])) # No single nums present
