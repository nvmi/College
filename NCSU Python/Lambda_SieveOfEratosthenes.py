# Lambda Sieve of Eratosthenes One-liners
# VERY INEFFECTIVE AND VERY SHORT

# P(n) - get a set of primes from 0 to n, D = (n > 2)
# R(n) - get a prime closest to integer n, that is less than n
# B(n) - get a boolean value representing validity of a statement that integer n is a prime
# N(n) - get a prime number n in sequence of primes from [1] = 2, (A000040 on OEIS) for reasonably large primes.

from functools import reduce 
from math import floor, log

# using P
# P = lambda n : set(range(2, n+1)).difference(x for y in range(2, n+1) for x in range(2, n+1) if x != y and x % y == 0)
# R = lambda n : reduce(lambda a,b : 0+b, P(n))
# B = lambda n : True if n in P(n+1) else False
# N = lambda n : list(P(n*floor(n*log(n,10))+1)))[n-1] if n < len(P(n*10)) else False

# as individual functions
P = lambda n : set(range(2, n+1)).difference(x for y in range(2, n+1) for x in range(2, n+1) if x != y and x % y == 0)) 
R = lambda n : reduce(lambda a,b : 0+b, set(range(2, n+1)).difference(x for y in range(2, n+1) for x in range(2, n+1) if x != y and x % y == 0))
B = lambda n : True if n in (set(range(2, n+2)).difference(x for y in range(2, n+2) for x in range(2, n+2) if x != y and x % y == 0)) else False
N = lambda n : list(set(range(2, n*10)).difference(x for y in range(2, n*10) for x in range(2, n*10) if x != y and x % y == 0))[n-1] if n < len(set(range(2, n*10)).difference(x for y in range(2, n*10) for x in range(2, n*10) if x != y and x % y == 0)) else False