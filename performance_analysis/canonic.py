#!/usr/bin/env python

import sys
import os
import collections

def usage():
    # print the usage of this python    
    print "Help: "
    print "python "+ sys.argv[0] + " datafile steps"
    return

if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
    usage()
    sys.exit()

log_file=sys.argv[1]

index = 0
int_word = []
for line in open(log_file, 'r'):
        int_word_data = line.split()[-1]
        int_word.insert(index, int_word_data)
        index = index + 1
        #int_word.insert(index, int(hex_word, 16))
        #index = index + 1

global_data = collections.Counter(int_word)
sort_data = global_data.items()
sort_data.sort()

g_key = list(global_data)
g_key.sort()
# output fromat for excel
#for key,value in sort_data:
#        print (str(key)+"\t"+str(value))

if len(sys.argv) < 3:
    usage()
    sys.exit()

# canonical distribution
length = len(sort_data)
step = sys.argv[2]
step_value = (int(g_key[-1]) - int(g_key[0])) // int(step)
print "The step is: "+str(sys.argv[2])+" The step value is: "+str(step_value)
new_data = {}
index = 0
per_value = 0
per_data = 0

for key,value in sort_data:
    if index < step:
        per_data = int(g_key[0])+step_value*index
        if int(key) < per_data:
            per_value += value
        else:
            new_data[per_data] = per_value
            per_value = 0
    index += 1
print new_data
#for key,value in new_data:
    #print (str(key)+"\t"+str(value))

