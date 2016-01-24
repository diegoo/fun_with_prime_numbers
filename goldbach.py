#!/usr/bin/env python

import sys
import itertools

def sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

def goldbach_summands(n):
    primes = sieve(n)
    candidates = itertools.combinations(primes, 2)
    for (a, b) in candidates:
        if (sum([a, b]) == n): 
            yield (a, b)

print list(goldbach_summands(int(sys.argv[1])))
