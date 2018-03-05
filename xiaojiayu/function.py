#!/usr/bin/env python

import os
import sys

# function 
def func_print():
    print "This is show how to use function"
    print "Note:"
    print "Use 'def'"
    print "such as: def my_function(): "
    print "tab and function body"
    print "invoke the my_function()"

# function parmeter
def love_func(name):
    print "Love the "+str(name)

# function return value
def l_sum(fir, sec):
    g = fir + sec
    return g

func_print()
love_func("ubuntu")
print l_sum(5, 8)

