# Create a function that returns an array with 20 values. For index X to Y, 
# have it be filled with the value of 1. For other values, have it be 0. 
# Assume that X is less than Y and also assume that both X and Y are below 20.

# For ex, generateArray(5,15) should return 
# an array of [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]

def generateArrayFrom(x,y):

    res = []
    i = 0
    if y > 20:
        y = 20
    while i <= 19:
        if i < x:
            res.append(0)
            i=i+1
        if i >= x and i <= y:
            res.append(1)
            i = i+1
        if i > y:
            res.append(0)
            i = i+1
    return res

print(generateArrayFrom(0, 25))


