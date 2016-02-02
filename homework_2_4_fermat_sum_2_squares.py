#!/usr/bin/env python
import math, itertools, sys

n = int(sys.argv[1])
numbers = range(1, int(math.sqrt(n)) + 1)

for (a, b) in itertools.combinations(numbers, 2):
    if a**2 + b**2 == n:
        print (a, b),
        break
