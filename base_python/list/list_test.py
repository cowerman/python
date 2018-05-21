

for num in range(1, 21, 1):  # range(1, 21, 1) == range(1, 21)
    print(num)
'''
nums = list(range(1, 1000001))
for num in nums:
    print(num)

print(max(nums))
print(min(nums))
print(sum(nums))
'''
new_list = list(range(1, 21, 2))
for num in new_list:
    print(num)

new_3 = list(range(3, 30, 3))
for num in new_3:
    print(num)

num_cube = [value**3 for value in range(1, 11)]
for num in num_cube:
    print(num)

my_foods = ['apple', 'banan', 'origine']
friend1_foods = my_foods
friend2_foods = my_foods[:]

my_foods.append('liulian')
friend1_foods.append('hongshu')
friend2_foods.append('ganzhe')

print(my_foods)
print(friend1_foods)
print(friend2_foods)


string = ['Three', 'items', 'from', 'the', 'middle', 'of', 'the', 'list', 'are', ':']
print(string[:3])
print(string[-3:])
print(string[2:7])

const_list = (80, 879, 27, 19, 2)
for const in const_list:
    print(const)

# const_list[0] = 90 # error as this object is const
const_list = (10, 20, 30, 40) # only cat re-init the const list, but cant only change one of the member
for const in const_list:
    print(const)
