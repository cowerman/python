
# 6-1 test
known_people = {
    'first_name':'john',
    'last_name':'danver',
    'age':'58',
    'city':'shanghai',
    }

print('Full name: {0}, {1}'.format(known_people['first_name'].title(), known_people['last_name'].title()))
print('{0}: {1}'.format('age'.title(), known_people['age']))
print('{0}: {1}'.format('city'.title(), known_people['city'].title()))

# 6-2 test
favorite_numbers = {
    'xiaorom':'9',
    'xiaohua':'4',
    'xiaolei':'3',
    'xiaomao':'7',
    'xiaogao':'2',
    'xiaojun':'8',
    }

for name,number in favorite_numbers.items():
    print('{0} favorite number is: {1}'.format(name.title(), number))

# 6-3 test
words_dict = {
    'print':'to output the discription of you want',
    'if':'to adjust the condition if it is wanted',
    'else':'will match "if" to use, the othe condition',
    'format':'to format the output the message on screen',
    'list':'which contain a seria of meta data which in the struct',
    }

for key,value in words_dict.items():
    print('{0}: {1}'.format(key, value.title()))

# 6-4 test
words_dict['for'] = 'loop the same code'
words_dict['in'] = 'will match the for to use'
words_dict['while'] = 'loop the same code'
words_dict['break'] = 'break with non-condition'
words_dict['bool'] = 'the valient of bool'

for key,value in words_dict.items():
    print('{0}: {1}'.format(key, value.title()))

# 6-5 test

# 6-6 test

# 6-7 test

known2_people = {
    'first_name':'dai',
    'last_name':'shuhua',
    'age':'28',
    'city':'shanxi',
    }
known3_people = {
    'first_name':'zhao',
    'last_name':'guer',
    'age':'5',
    'city':'xinzhang',
    }
people = [known_people, known2_people, known3_people]
for one_people in people:
    print('Full name: {0}, {1}'.format(one_people['first_name'].title(), one_people['last_name'].title()))
    print('{0}: {1}'.format('age'.title(), one_people['age']))
    print('{0}: {1}'.format('city'.title(), one_people['city'].title()))

# 6-8 test

# 6-9 test
favorite_places = {
    'john':['quanzhou', 'huian', 'hangzhou'],
    'steve':['beijing', "xia'an"],
    'boble':['tianjin']
    }
for name,places in favorite_places.items():
    print("{0} favorite the places:".format(name.title()))
    for place in places:
        print('\tplace: {0}'.format(place.title()))

# 6-10 test

# 6-11
cities = {
    'nanchang':{
        'country':'china',
        'population':'675',
        'fact':'big',
        },

    'shangrao':{
        'country':'china',
        'population':'321',
        'fact':'medium',
        },

    'jiujiang':{
        'country':'china',
        'population':'123',
        'fact':'small',
        },
    }

for city_name,details in cities.items():
    print("The {0} city detail below:".format(city_name))
    print("\t{0}: {1}".format('country'.title(), details['country']))
    print("\t{0}: {1}".format('populatin'.title(), details['population']))
    print("\t{0}: {1}".format('fact'.title(), details['fact']))
