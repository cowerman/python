#!/usr/bin/env python

import sys
import os
import collections
from collections import OrderedDict

def usage():
    # print the usage of this python    
    print "Help: "
    print "python "+ sys.argv[0] + " datafile steps"
    return

if len(sys.argv) < 3:
    usage()
    sys.exit()

log_file=sys.argv[1]

index = 0
int_word = []

fd = open(log_file, 'r')
for line in fd:
        int_word_data = int(line.split()[-1])
        int_word.insert(index, int_word_data)
        index = index + 1
        #int_word.insert(index, int(hex_word, 16))
        #index = index + 1
fd.close()

sort_data = collections.Counter(int_word).items()
sort_data.sort()

g_key = list(collections.Counter(int_word))
g_key.sort()

#free int_word
int_word = []

# output fromat for excel
#for key,value in sort_data:
#        print (str(key)+"\t"+str(value))

# canonical distribution
length = len(sort_data)
step = sys.argv[2]
step_value = (int(g_key[-1]) - int(g_key[0])) / int(step)
#print "The step is: "+str(sys.argv[2])+" The step value is: "+str(step_value)
new_data = {}
per_value = 0
per_data = 0

per_data = int(g_key[0]) + step_value
#free g_key
g_key = []

for key,value in sort_data:
    #print "key: " + str(key) + "    value: " + str(value) + "    per_data: " + str(per_data) + "    per_value: " + str(per_value)
    if int(key) < per_data:
        per_value += value
    else:
        new_data[per_data] = per_value
        per_value = 0
        per_data += step_value

        while True:
            if int(key) < per_data:
                per_value += value
                break
            else :
                new_data[per_data] = per_value
                per_data += step_value
                continue

new_data[per_data] = per_value

items = new_data.items()
items.sort()
for k, v in items:
    print str(k)+","+str(v)
