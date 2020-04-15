#!/usr/bin/python

import sys
import math


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    ways = 0
    # Base case
    if n == 1 or n == 0:
        return 1



    return eating_cookies(n-1) + eating_cookies(n-2)


​
def fib(n, cache=None):
    if cache is None:
        cache = {}
    # Base case
    if n <= 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        answer = fib(n-1, cache) + fib(n-2, cache)
        cache[n] = answer
        # Recursive call, should move toward base case
        return answer

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
