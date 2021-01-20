# Function for nth fibonacci number - Dynamic Programming 
# Given a number n, print n-th Fibonacci Number. 

def fibonacci(n):
    if n == 0:
        return "Error"
    elif n ==1:
        return 0
    elif n <= 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# testing for the "nth" fibonacci sequence number
print(fibonacci(1)) #0
print(fibonacci(2)) #1
print(fibonacci(3)) #1
print(fibonacci(4)) #2
print(fibonacci(6)) #5