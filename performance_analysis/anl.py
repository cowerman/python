#!/usr/bin/python

import sys
import os
import collections

def usage():
    # print the usage of this python    
    print "Help: "
    print "python "+ sys.argv[0] + "input output"
    return

# first step
def grep2out():
    # this function will grep key and ouput file

    return
 
#if len(sys.argv) < 3 or not os.path.isfile(sys.argv[1]):
if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
    usage()
    sys.exit()

log_file=sys.argv[1]


try:
	logs = open(log_file, 'r')
	lines = logs.readlines()
except IOError:
    print "File is not accessible!"

index = 0
int_word = []
word_dict = {}
for line in lines:
	hex_word = line[58:-1]
	int_word.insert(index, int(hex_word, 16))
	index = index + 1

global_data = collections.Counter(int_word)
sort_data = global_data.items()
sort_data.sort()

# output fromat for excel
for key,value in sort_data:
	print (str(hex(key))+" "+str(value))

logs.close()
