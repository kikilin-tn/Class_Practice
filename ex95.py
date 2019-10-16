"""
Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166).
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly,
and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0.
"""
class User():
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = login_attempts

    def describe_user(self):
        user_info = 'The user is ' + self.first_name  + ' ' + self.last_name
        print(user_info)

    def greet_user(self):
        msg = 'Welcome back! '+ self.first_name + ' ' + self.last_name + '.' + '\n'
        print(msg)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
print('\n')
eric = User('Mary', 'Lin', 1)
eric.greet_user()

print('making 3 login attempts..')
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print('  Login attempts: ' + str(eric.login_attempts))

print('resetting the login...')
eric.reset_login_attempts()
print('  Login attempts: ' + str(eric.login_attempts))
