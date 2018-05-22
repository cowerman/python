
car='subaru'
print('Is car == "subaru" ? I predict True.')
print(car == 'subaru')
print('Is car == "Audi" ? I predict True.')
print(car == 'Audi')

a = 'taste good'
b = 'taste Good'

if a == b:
    print("a equal b")
else:
    print("a not equal b")
    if a.lower() == b.lower():
        print("lower a equal lower b")

a = 20
b = 90
print(a > b)
print(a < b)
print(a!=b)
print(a==b)
print(a>=b)
print(a<=b)

if a < b and a < 30:
    print("and test")

if a > b or a >10:
    print("or test")


lw_list = ['man', 'men', 'women', 'woman', 'femal', 'cower']
a = 'cower'
if a in lw_list:
    print(a + ' in list')
else:
    print(a + ' not in list')

if a not in lw_list:
    print(a + ' not in list')
else:
    print(a + ' in list')
