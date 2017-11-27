#8.4 passing a list
def greet_users(names):
    """向列表中的每一位用户发出简单的问候"""
    for name in names:
        msg="Hello, "+name.title()+"!"
        print(msg)
usernames=['nanamin','miona','nachan']
greet_users(usernames)
