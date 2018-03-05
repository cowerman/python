#!/usr/bin/python 
#encoding=utf-8

def hanoi(n, x, y, z):
    #x表示第x根柱子，y表示第y根柱子，z表示第z根柱子
    if n==1:
        print x,'-->',z
    else:
        #将前n-1个盘子移动到y:
        hanoi(n-1, x, z, y)
        print x, '-->', z    #x柱子移动到z上
        #将y上的n-1个盘子移动到z上 
        hanoi(n-1, y, x, z)
import sys 

hanoi(int(sys.argv[1]), 'x', 'y', 'z')
