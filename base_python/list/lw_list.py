
# use list: modify/del /pop/remove/append/insert/sort/reverse/len()

# append/insert:
#   append: lw_list.append('x')------ insert: lw_list.insert(index_num, 'str1')
# del/pop/remove:
#   del: del lw_list[index_num]------ pop: lw_list.pop(index_num)/lw_list.pop()
#   remove: lw_list.remove(value)
# sort/sorted/reverse
#   sort: lw_list.sort(reverse=False) --> sort the list from litter to big and forever
#   sorted: sorted(lw_list) --> tmp sorted lw_list 
#   reverse: lw_list.reverse()
# len():
# len(lw_list)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
        'z']

# access of the list
c = alpha[2]
print(alpha[0])
print(c)
print(alpha)
print(alpha[-1])

friends = ['yang,ling', 'wensheng', 'tianhua', 'zhong,ming', 'du,mingze', 
        'tanwei', 'jin, zhebin', 'zhuo,zhikai', 'li, jinjue']

for friend in friends:
    print(friend.title()+", good to see you again!")

alpha_cpy = alpha
print(alpha)

# modify the alpha_cpy list
alpha_cpy[0] = 'x'
print(alpha_cpy)
lw = ['liu', 'wei']

# insert a member or another list to the alpha_cpy list
alpha_cpy.append(lw)
alpha_cpy.append('z')
print(alpha_cpy)
alpha_cpy.insert(0, 'a')
print(alpha_cpy)
alpha_cpy.insert(2, 'a')
alpha_cpy.insert(0, lw)
print(alpha_cpy)

# del a member or another list from the alpha_cpy list
del alpha_cpy[2]
print(alpha_cpy)
alpha_cpy.pop() # del last member
print(alpha_cpy)
#get_poped = alpha_cpy.pop() # equal alpha_cpy.pop(-1)
get_poped = alpha_cpy.pop(-1)
print(alpha_cpy)
print("Pop got:", get_poped)

# del with value not index
alpha_cpy.remove(lw)
alpha_cpy.remove('a')
print(alpha_cpy)

# sort method to sort list forever
alpha_cpy.reverse()
print(alpha_cpy)
alpha_cpy.sort(reverse=False)
print(alpha_cpy)
alpha_cpy.sort(reverse=True)
print(alpha_cpy)

alpha_as_cpy = sorted(alpha_cpy)
print(alpha_as_cpy)

# len() to list
alpha_len = len(alpha_cpy)
print("Alphan Lenght: ",str(alpha_len))

# convert range(start_num, end_num) to list with function list()
# range() end_num need to add externation 1
numbers = list(range(1, 10))    # 1 2 .. 9
print(numbers)
even_nums = list(range(2, 11, 2))
print(even_nums)
ord_nums = list(range(1, 11, 2))
print(ord_nums)

# list jiexi 1. [square**2  2. for square in range(x,x1)]
squares = [square**2 for square in range(1,11)]
print(squares)
