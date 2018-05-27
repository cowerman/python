
# dict = {'key1':'value1', 'key2':value2}

# alien_0 as dict
alien_0 = {'color':'green', 'points':5}

# when autogenate tons of key:value, often need the empty dict
data_list = {}
data_list['1'] = 9
data_list['k'] = 'blak K'

print(data_list)
# access dict value
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

#  override the dict key:value
alien_0 = {'color1':'grey', 'points1':6}
print(alien_0)

#  add the dict key:value
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# modify the dict value by key
alien_0['x_position'] = 10
alien_0['y_position'] = 90
print(alien_0)

# delete the dict by key with del function
alien_0['z_position'] = 20
print(alien_0)
del alien_0['z_position']
print(alien_0)

# walk all the datas with method .items()
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    'jack':'c++',
    'mark':'java',
    'jason':'asm',
    }
print("\twalk the data by key,value")
for key,value in favorite_languages.items():
    print("Name: {0},\tFavorite: {1}".format(key.title(), value.title()))

#  walk all the keys with method .keys()
print("\twalk the data by .keys()")
for key in favorite_languages.keys():
    print("{0} was been caculate".format(key.title()))

print("\twalk the sorted() .keys")
for key in sorted(favorite_languages.keys()):
    print("{0} was been caculate".format(key.title()))

# walk all the values wiht method .values()
print("\twalk the data by .values()")
for value in favorite_languages.values():
    print("{0} language in the list".format(value.title()))

# walk all the data values and delte re-valute with function set()
print("\twalk and delate the copy values wiht function of set()")
for value in set(favorite_languages.values()):
    print("{0} language in the list".format(value.title()))

# dictorany of arrey [arrey contain dictorany]
alien_0 = {'color':'black', 'points':5, 'speed':'slow'}
alien_1 = {'color':'red', 'points':6, 'speed':'high'}
alien_2 = {'color':'grey', 'points':7, 'speed':'slow'}
alien_3 = {'color':'white', 'points':6, 'speed':'slow'}
alien_4 = {'color':'brown', 'points':7, 'speed':'hight'}

aliens = [alien_0, alien_1, alien_2, alien_3, alien_4]

# append the 25 aliens to the aliens list
for alien in range(5):
   aliens.append(alien_2)

# print the all aliens
print(str(aliens)+'\n')

# print the 5 alien
for alien in aliens[:5]:
    print(alien)

# print the len of alien
print("Total length of aliens: {0}".format(len(aliens)))

# arrey of dictorany [dictorany contain of arrey]
pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra', 'extra cheese'],
    }

print('You ordered a '+pizza['crust']+'-curst pizza'+
    'with the following toppings:')
for topping in pizza['toppings']:
    print(topping+'\t')

# dictory of dictory [dictory contain of dictorany]
usrs = {
    'aient_0':{
        'first':'maijelun',
        'last':'dikanong',
        'location':'princeton'
        },
    'alient_1':{
        'first':'john',
        'last':'danver',
        'location':'ameraca',
        },
    }

for usr,informations in usrs.items():
    print("{0}'s information:".format(usr.title()))
    print('\tFull name: {0}'.format(informations['first'].title()+', '+informations['last'].title()))
    print('\tLocation: '.format(informations['location'].title()))


