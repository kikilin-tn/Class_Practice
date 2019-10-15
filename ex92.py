"""
Start with your class from Exercise 9-1.
Create three different instances from the class,
and call describe_restaurant() for each instance.
"""
from ex91 import Restaurant

cafe = Restaurant('mini store', 'bread', "10 o'clock")
cafe.describe_restaurant()

store = Restaurant('disney store', 'mickey', "10 o'clock")
store.describe_restaurant()
store.open_restaurant()
