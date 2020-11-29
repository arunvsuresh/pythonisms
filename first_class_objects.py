def func1(name):
    return f"hello {name}"

def func2(name):
    return f"{name}, you're so awesome"

# passing in functions to other functions
def func_calling_func_as_first_class_obj(first_class_obj_func):
    return first_class_obj_func('arun')

def greet(text):
    return text.upper() + "!"

def func_acting_as_variable(func):
    var = func
    return var('text')
