#!/usr/bin/env python

import os
import sys

b = "I love all of study"
b = list(b)

c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
c = list(c)

print b
print c
print max(b), max(c)
print min(b), max(c)
print sum(c)
#print sum(b), sum(c)
print sorted(c), sorted(b)
print list(reversed(c)) # list ()

# zip
ll = (1, 2, 3, 4, 5, 6, 7, 8)
ww = (4, 5, 6, 7, 8)
print zip(ll, ww)
