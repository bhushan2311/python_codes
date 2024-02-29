# Factorial by recursion
"""def rec(n):
    # if(n==1 or n==0):
    #      return 1
    # else:
    #     return n * rec(n-1)          # by recursion

    fact=1
    for i in range(n):                 # by iteration
        fact=fact*(i+1)
    return fact

n=int(input("Enter the number: "))
print(rec(n))"""

# Fibonacci series by recursion
def fib(n):
    """a no. in the series is the sum of previous 2 no.s
        for eg. 0 1 1 2 3 5 8 13..."""
    if(n==1 or n==2):
         return 1
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Enter the number: "))
print(fib(n))
