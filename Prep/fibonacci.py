n=10
def fib(n):
    #base case
    if n==0 or n==1: return n
    #check cache
    if cache[n]!=None: return cache[n]
    #setting cache
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

cache = [None]*(n+1)
print(fib(10))