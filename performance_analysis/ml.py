#!/usr/bin/python

import sys
import os
import re

f = open("./cat_log", 'r')
lines = f.readlines()

for line in lines:
	key_word = line[58:-1]

dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
dict= sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
print dict
