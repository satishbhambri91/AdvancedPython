# def outer_function(msg):
#     message = msg
#
#     def inner_function():
#         print message
#     return inner_function

# my_func = outer_function('Satish')
# my_func2 = outer_function('Space')
#
# my_func()
# my_func2()

def decorator_function(original_function):
    def wrapper_function():
        print ('Wrapper executed this before {}'.format(original_function.__name__))
        return original_function()

    return wrapper_function

@decorator_function
def display():
    print 'Display function executed !'

display()
# hi_func = decorator_function('Hi !!')
# bye_func = decorator_function('Bye !!')

# hi_func()
# bye_func()

# decorated_display = decorator_function(display)
# decorated_display()
