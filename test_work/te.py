#!/usr/bin/env python3

def method_1(n) :
    last_is_one = False
    this_is_one = False
    while n > 0:
        this_is_one = n % 2 
        if this_is_one and last_is_one:
            return True
        n = n >> 1
        last_is_one = this_is_one
    return False

def method_2(value):
    bit_1_cnt = 0
    tmp_val = value
    is_contiguous = False

    if value == 0:
        is_contiguous = True

    while tmp_val > 0:
        tmp_val &= (tmp_val - 1)
        bit_1_cnt += 1

    if bit_1_cnt == 1:
        is_contiguous = True
        return is_contiguous

    if value & (value >> 1) > 0:
        is_contiguous = True

    return is_contiguous

def is_contiguous_bit_set(value):
    bit_1_cnt = 0
    tmp_val = value
    cur_bit = False
    pre_bit = False
    pre_zero_bit = True
    is_contiguous = False
    contiguous_cnt = 0

    if value == 0:
        is_contiguous = True
        return is_contiguous

    while tmp_val > 0:
        tmp_val &= (tmp_val - 1)
        bit_1_cnt += 1

    for shift_i in range(16):
        mask = (0x1 << shift_i)
        if value & mask:
            cur_bit = 1
            if cur_bit and pre_bit:
                contiguous_cnt += 1
        else:
            cur_bit = 0

        pre_bit = cur_bit

    if bit_1_cnt == contiguous_cnt or bit_1_cnt == 1:
        is_contiguous = True

    print("--debug: value:{}, 1_cnt:{}, contiguous_cnt:{}".format(value, bit_1_cnt, contiguous_cnt))
    return is_contiguous

a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#print("{},{}".format(a,method_1(a)))
for i in a:
    print("{},{}".format(i,is_contiguous_bit_set(i)))
