
# 9-1 test:

class Resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        print("The resturant name is {0}".format(self.resturant_name.title()))
        #print("The resturant cuisne type {0}".format(self.cuisine_type))

    def open_resturant(self):
        print("The resturant is opening now")

    def set_number_served(self, numbers):
        if numbers < 0:
            print("Un-logic integer")
            return False
        else:
            self.number_served = numbers

    def increment_number_served(self, numbers):
        if numbers < 0:
            print("Un-logic integer")
            return False
        else:
            self.number_served += numbers

    def get_number_served(self):
        print("The resturant serverd people: {0}".format(self.number_served))

resturant = Resturant('He Ping Resturant', 1990)
print("The resturant is {0}".format(resturant.resturant_name.title()))
print("The resturant type {0}".format(resturant.cuisine_type))

resturant.describe_resturant()
resturant.open_resturant()

# 9-2 test:
re1 = Resturant('Hai di lao', 2007)
re2 = Resturant('Yue cai xi', 2010)
re1.describe_resturant()
re2.describe_resturant()

# 9-3 test:
class User():

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.login_attempts = 0

    def describe_user(self):
        print("This is {0} {1}".format(self.first_name.title(), self.last_name.title()))

    def greet_user(self):
        print("Hello {0} {1}, welcom!".format(self.first_name.title(), self.last_name.title()))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print("The login attempts: {0}".format(self.login_attempts))

u1 = User('chen', 'jack')
u2 = User('zhou', 'jay')
u3 = User('lu', 'qi')

u_list = [u1, u2, u3]
for u_m in u_list:
    u_m.describe_user()
    u_m.greet_user()

# 9-4 test:
print("The resturant serverd people: {0}".format(resturant.number_served))
resturant.number_served = 90
print("The resturant serverd people: {0}".format(resturant.number_served))
resturant.set_number_served(180)
resturant.increment_number_served(90)
resturant.get_number_served()

# 9-5 test:
u4 = User('John', 'danver')
u4.show_login_attempts()
u4.increment_login_attempts()
u4.increment_login_attempts()
u4.show_login_attempts()
u4.reset_login_attempts()
u4.show_login_attempts()

# 9-6 test:
class IceCreamStand(Resturant):
    def __init__(self, r_name, t_type):
        super().__init__(r_name, t_type)
        self.flavors = ['bulue bearry', 'banana', 'oriange', 'apple']

    def show_icecream(self):
        print("There are below flavors:")
        for ice in self.flavors:
            print("\t{0}".format(ice.title()))

my_ice = IceCreamStand('Heqing', '1009')
my_ice.show_icecream()

# 9-7 test:
class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The privileges are:")
        for privilege in self.privileges:
            print("\t{0}".format(privilege.title()))

admin = Admin("Lu", "ben")
admin.show_privileges()

# 9-8 test:
class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delte post', 'can ban user']

    def show_privileges(self):
        print("The privileges are:")
        for privilege in self.privileges:
            print("\t{0}".format(privilege.title()))
class Cdmin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privileges = Privileges()


cdmin = Cdmin('lu', 'qu')
cdmin.privileges.show_privileges()

# 9-9 test:


