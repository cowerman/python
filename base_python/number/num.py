#import os
#import sys

a = 9.0
b = 8
c = 10
name = "Han, Mei"
age = 28

lw_list = list(range(1, 101, 1)) # equal list(range(1, 101))

print(a*b)
# ** different between with * 
print((a+1)**b)
print(name+"\nage:"+str(age))
print("a/b="+str(a)+"/"+str(b)+"="+str(a/b))
print("c/b="+str(c)+"/"+str(b)+"="+str(c/b))

# min/max/sum  compare the min/max/sum of the list given
print(lw_list)
print(min(lw_list))
print(max(lw_list))
print(sum(lw_list))
