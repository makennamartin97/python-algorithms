# Objectives
# Create a function that accepts a number as an input. Return a new list that 
# counts down by one, from the number (as the 0th element) down to 0 (as the 
# last element).

#For example, countdown(5) should return [5,4,3,2,1]

def Countdown(n):
    new = []
    while n >= 0:
        new.append(n)
        n=n-1
    

    return new      

# testing
print(Countdown(34))