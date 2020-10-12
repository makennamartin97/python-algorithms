import random

class UsefulLib:

    def filterRange(self, list, min, max):
        for k in range(len(list)-1):
            if list[k] < min:
                list.remove(list[k])
            if list[k] > max:
                list.remove(list[k])
            
        return list
l = UsefulLib()

print(l.filterRange([1,3,5,7,9], 2,8) )
print(l.filterRange([1,3,5,7,9], 4,6))