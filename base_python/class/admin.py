
class User():

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        self.login_attemtps = 0

    def describe_user(self):
        print("This is {0} {1}".format(self.first_name.title(), self.last_name.title()))

    def greet_user(self):
        print("Hello {0} {1}, welcom!".format(self.first_name.title(), self.last_name.title()))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



class Admin(User):

    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privileges = ['can add post', 'can delte post', 'can ban user']

    def show_privileges(self):
        print("The privileges are:")
        for privilege in self.privileges:
            print("\t{0}".format(privilege.title()))

