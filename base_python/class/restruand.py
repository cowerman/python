
class Resturant():
    def __init__(self, resturant_name, t_type):
        self.resturant_name = resturant_name
        self.t_type = t_type

    def describe_resturant(self):
        print("The resturant name is {0}".format(self.resturant_name.title()))

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
