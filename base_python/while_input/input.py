
'''
# 7-1 test: 
get = input("What can i do for you: ")
if get == 'LeiNuo':
    print("yes, i will show you " + get)
else:
    print("Let me see if I can find you Subaru")

# 7-2 test:
check_table = input("How many people for launch: ")
if int(check_table) > 8:
    print("We have not enough tables for your guys")
else:
    print("We have enough table for your guys")

# 7-3 test:
mod_10 = input("Please input a number: ")
if int(mod_10) % 10 == 0:
    print("Your number is mod of 10")
else:
    print("Your number is not mod of 10")
# 7-4 test:
pizza_addi = []
get_in = 'init'
get_in = input("What's you pizza to add: ")
while get_in != '' and get_in != 'quit':
    print("We will add the "+get_in+" in pizza")
    get_in = input("What's you pizza to add: ")


# 7-5 test:
age = input("How old are you: ")
while age != 'quit':
    if int(age) < 3:
        print("You are a child, you are free to watch movie")
    elif int(age) < 12:
        print("You are a teanger, ticket cost: 10$")
    else:
        print("You are young, ticket cost: 15$")
    
    age = input("How old are you: ")
# 7-6 test:

# 7-7 test:
while True:
    print("Here is dead loop")

# 7-8 test:
sandwich_orders = ['beef sandwich', 'pork sandwich', 'vegtable sandwich']
finished_sandwich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I'm "+sandwich+", you like it")
    finished_sandwich.append(sandwich)

print("The finished sandwich:")
for s_wich in finished_sandwich:
    print("\t{0}".format(s_wich))


# 7-9 test:

sandwich_orders = ['beef sandwich', 'op', 'op', 'pork sandwich', 'vegtable sandwich', 
        'mongon sandwich', 'branan sandwich', 'orignal sandwich', 'op', 'op']
finished_sandwich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I'm "+sandwich+", you like it")
    finished_sandwich.append(sandwich)

print("The finished sandwich:")
for s_wich in finished_sandwich:
    print("\t{0}".format(s_wich))

sold = False
sa = 'op'
print("The sandwich of 'op' sold out")
while sa in finished_sandwich:
    finished_sandwich.remove(sa)

print(finished_sandwich)
'''

# 7-10 test:

famous_places = []

place = input("If you visit on place in the world, where would you go? ")
while place != "quit" and place != '':
    famous_places.append(place)
    place = input("If you visit on place in the world, where would you go? ")

print("Here is the details of result:")
print(famous_places)
    
