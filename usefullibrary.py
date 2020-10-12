import random

class UsefulLib:

    def multiply(self, list, x):
        l = len(list)
        for i in range(l):
            list[i] = list[i] * x
        return list
    
    def filterRange(self, list, min, max):
        res = []

        for k in list:
            num = k
            if num > min and num < max:
                res.append(k)

            
        return res

    def shuffle(self, list, x):
        l = len(list)
        index = random.randint(0, l)
        for i in range(x):
            temp = list[index]
            list[index] = list[l-index]
            list[l-index] = temp
        return list
    
    def randomBetween(self,x,y,z):
        return random.randrange(x,y,z)



    
lib = UsefulLib()

# testing
print(lib.multiply([2,10,5,3], 7) ) # [14, 70, 35, 21]
print(lib.filterRange([1,3,5,7,9], 2,8) ) # [3, 5, 7]
print(lib.filterRange([1,3,5,7,9], 4,6) ) # [5]
#print(lib.shuffle([1,3,5,7,9,11], 3) ) # [1, 3, 9, 7, 5, 11]
#print(lib.shuffle([1,3,5,7,9,11], 0) ) # [1, 3, 5, 7, 9, 11]

print(lib.randomBetween(100,200,7))

