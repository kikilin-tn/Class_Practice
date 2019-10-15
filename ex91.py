"""
Make a class called Restaurant.
The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of information,
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
"""
class Restaurant():

    def __init__(self, name, cuisine_type, open_time):
        self.name = name
        self.cuisine_type = cuisine_type
        self.open_time = open_time

    def describe_restaurant(self):
        msg = self.name + ' serves the wonderful ' + self.cuisine_type + ' cuisine.'
        print(msg)

    def open_restaurant(self):
        msg = self.name + ' restaurant is open at '+ self.open_time + ' come on in.'
        print( msg)

restaurant = Restaurant('woo','tai', "7 o'clock")
print(restaurant.name)
print(restaurant.cuisine_type)
print(restaurant.open_time)

restaurant.describe_restaurant()
restaurant.open_restaurant()
