"""
An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits(繼承) from the Restaurant class
you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171).
Eitehr version of the class will work; just pick the one you like better.
Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
"""
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = self.name + ' serves the wonderful ' + self.cuisine_type + '.'
        print('\n'+ msg +'\n')

    def open_restaurant(self):
        msg = self.name + ' restaurant is open! Come on in.'
        print( msg)

class IceCreamStand(Restaurant):  #類別的第一個字母要大寫
    def __init__(self, name, cuisine_type='ice cream'):
        super().__init__(name, cuisine_type)#父繼承
        self.flavors = []  #可裝不同口味的空清單

    def show_flavors(self):
        print('We served the following flavors: ')
        for flavor in self.flavors:
            print('-' + flavor.title())

goldstone = IceCreamStand('goldstone')
goldstone.flavors = ['vanilla','chocolate','strawberry']

goldstone.describe_restaurant()
goldstone.open_restaurant()
goldstone.show_flavors()
