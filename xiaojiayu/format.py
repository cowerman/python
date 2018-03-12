#!/usr/bin/env python

import os
import sys

print "%c" % (97)
print "%c" % 98
print "%-10d" % 68
print "%10d"  % 69
print "%10s" % "i love"
print "%-10s" % "n love"


print "%010d" % 67
print "%2f" % 78.96

# location par
print "{0} love {1} {2}".format("I", "ubuntu", "too")

print "{a}, love {b} {c}".format(a="I", b="ubuntu", c="also")

print "Total: {0:.1f}{1}".format(27.66, "GB")
