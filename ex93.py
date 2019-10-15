"""
Make a class called User. Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
"""
class User():
    def __init__(self, first_name, last_name, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.upper()

    def describe_user(self):
        user_info = 'The user is ' + self.first_name  + ' ' + self.last_name
        print(user_info)
        print('Location: ' + self.location)

    def greet_user(self):
        msg = 'Welcome back! '+ self.first_name + ' ' + self.last_name + '.' + '\n'
        print(msg)

user = User('Lin', 'Amy', 'TC')
user.describe_user()
user.greet_user()

user = User('Yang', 'Mary', 'TP')
user.describe_user()
user.greet_user()
