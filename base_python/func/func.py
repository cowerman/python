
'''
# 8-1 test:
def display_message():
    print("In this charpter, I learned how to use function")

display_message()

# 8-2 test:
def favorite_book(title):
    print("One of my favroite book is "+"\""+title.title()+"\"")

fav_book = input("What is you favorite book? ")
favorite_book(fav_book)

# 8-3 test:

def make_shirt1(size, log):
    print("The T shirt size is {0}, we also need the beatuiful \
log '{1}' on it".format(size, log.title()))

make_shirt1(20, "i love you")
make_shirt1(size=90, log='i O U')

# 8-4 test:
def make_shirt2(size='big', log='I love python'):
    print("The T shirt size is '{0}', we also need the beatuiful \
log '{1}' on it".format(size.title(), log.title()))

make_shirt2()
make_shirt2(size='medium')
make_shirt2(log='i o L')

# 8-5 test:

# 8-6 test:
def city_country(city, country):
   print(str(city).title()+','+str(country).title())

city_country('sichuan', 'china')
city_country('anhui', 'china')
city_country('xianxi', 'china')

# 8-7 test:
song_infos = {}
def make_album(sinnger, album):
    song_infos[sinnger] = album

make_album('John danver', 'take my home')
make_album('Meleasy', 'go out')
make_album('fei', 'what')

for name,abum in song_infos.items():
    print("\tName: {0}, Album: {1}".format(name.title(), abum.title()))
# 8-8 test:

song_infos1 = {}
def make_album(sinnger, album):
    song_infos1[sinnger] = album

make_album('John danver', 'take my home')
make_album('Meleasy', 'go out')
make_album('fei', 'what')

while True:
    get_name = input("What is the sinnger's name: ")
    if get_name == '' or get_name == 'quit':
        print('Terminate to input the message')
        break
    get_album = input("what is the sinnger's ablbum: ")
    if get_album == '' or get_album == 'quit':
        print('Terminate to input the message')
        break
    make_album(get_name, get_album)

for name,abum in song_infos1.items():
    print("\tName: {0}, Album: {1}".format(name.title(), abum.title()))

# 8-9 test:

def show_magics(mags):
    for mag in mags:
        print('The magic name: {0}'.format(mag.title()))

magics = ['yuqi', 'dawei', 'mock', 'jelly', 'killy']
show_magics(magics)


'''
# 8-10 test:

def show_magics(mags):
    for mag in mags:
        print('{0}'.format(mag.title()))

def make_great(ms):
    for mag in ms:
        ms.append('the great')
    show_magics(ms)

magics = ['yuqi', 'dawei', 'mock', 'jelly', 'killy']
show_magics(magics)
make_great(magics)
