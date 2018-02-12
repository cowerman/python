#!/usr/bin/env python

import os
import sys
import commands

cpu_prefix        = "logs/bench_log/cpu/cpu_"
gpu_prefix        = "logs/bench_log/gpu/gpu_"
rnd_read_prefix   = "logs/bench_log/mem/mem_rnd_read_"
seq_read_prefix   = "logs/bench_log/mem/mem_seq_read_"
rnd_write_prefix  = "logs/bench_log/mem/mem_rnd_write_"
seq_write_prefix  = "logs/bench_log/mem/mem_seq_write_"

cpu_num           = commands.getstatusoutput("ls -l "+str(cpu_prefix)+"* | wc -l")
gpu_num           = commands.getstatusoutput("ls -l "+str(gpu_prefix)+"* | wc -l")
mem_rnd_read_num  = commands.getstatusoutput("ls -l "+str(rnd_read_prefix)+"*  | wc -l")
mem_seq_read_num  = commands.getstatusoutput("ls -l "+str(seq_read_prefix)+"*  | wc -l")
mem_rnd_write_num = commands.getstatusoutput("ls -l "+str(rnd_write_prefix)+"* | wc -l")
mem_seq_write_num = commands.getstatusoutput("ls -l "+str(seq_write_prefix)+"* | wc -l")

'''
# debug to print the number of each log files
print cpu_num
print gpu_num
print mem_rnd_read_num
print mem_seq_read_num
print mem_rnd_write_num
print mem_seq_write_num
'''
cpu_list = []
gpu_list = []
mem_rnd_read_list  = []
mem_rnd_write_list = []
mem_seq_read_list  = []
mem_seq_write_list = []

# skip first two data for eache log file by default
skip = 2

for i in range(5):
    # differentt type log file
    i += 1
    if i == 1:
        file_num   = cpu_num
        log_prefix = cpu_prefix
    if i == 2:
        file_num   = gpu_num
        log_perfix = gpu_prefix
    if i == 3:
        file_num   = mem_rnd_read_num
        log_prefix = rnd_read_prefix
    if i == 4:
        file_num   = mem_seq_read_num
        log_prefix = seq_read_prefix
    if i == 5:
        file_num   = mem_rnd_write_num
        log_prefix = rnd_write_prefix
    if i == 6:
        file_num   = mem_seq_write_num
        log_prefix = seq_write_prefix

    # the number for the same type file
    for log_i in range(int(file_num[1])):
        log_file =  log_prefix + str(log_i+1)

    # anl the specify the log file
        index = 1
        for row in open(log_file, 'r'):
            if len(row) < 3:
                continue
            # cpu perfermence
            if i == 1:
                if row.split()[1] == "time:":
                    if index < skip:
                        index += 1
                        continue
                    cpu_list.insert(index, row.split()[2])
            if i == 2:
                if row.split()[1] == "Score:":
                    if index < skip:
                        index += 1
                        continue
                    gpu_list.insert(index, row.split()[2])
            if i == 3:
                if row.split()[2] == "transferred":
                    if index < skip:
                        index += 1
                        continue
                    rnd_read = row.split()[3].lstrip('(').rstrip(')')
                    mem_rnd_read_list.insert(index, rnd_read)
            if i == 4:
                if row.split()[2] == "transferred":
                    if index < skip:
                        index += 1
                        continue
                    seq_read = row.split()[3].lstrip('(').rstrip(')')
                    mem_seq_read_list.insert(index, seq_read)
            if i == 5:
                if row.split()[2] == "transferred":
                    if index < skip:
                        index += 1
                        continue
                    rnd_write = row.split()[3].lstrip('(').rstrip(')')
                    mem_rnd_write_list.insert(index, rnd_write)
            if i == 6:
                if row.split()[2] == "transferred":
                    if index < skip:
                        index += 1
                        continue
                    seq_write = row.split()[3].lstrip('(').rstrip('(')
                    mem_seq_write_list.insert(index, row.split()[3])
            index += 1

# sort the list

# abandon the lowest and the highest value

print cpu_list
print gpu_list
"""
# cal the averager values
cpu_avg = sum(float(y) for y in cpu_list) / len(cpu_list)
gpu_avg = sum(float(y) for y in gpu_list) / len(gpu_list)
mem_rnd_read_avg = sum(float(y) for y in mem_rnd_read_list) / len(mem_rnd_read_list)
mem_seq_read_avg = sum(float(y) for y in mem_seq_read_list) / len(mem_seq_read_list)
mem_rnd_write_avg = sum(float(y) for y in mem_rnd_write_list) / len(mem_rnd_write_list)
mem_seq_write_avg = sum(float(y) for y in mem_seq_write_list) / len(mem_seq_write_list)

# output the average value data
print "CPU take time(s):                  "+str(cpu_avg)
print "GPU Score(fps):                    "+str(gpu_avg)
print "MEM random read  speed(MB/S):      "+str(mem_rnd_read_avg)
print "MEM random write speed(MB/S):      "+str(mem_rnd_read_avg)
print "MEM sequential read  speed(MB/S):  "+str(mem_rnd_read_avg)
print "MEM sequential write speed(MB/S):  "+str(mem_rnd_read_avg)
"""

