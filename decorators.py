# first class objects
def func1(name):
    return f"hello {name}"

def func2(name):
    return f"{name}, you're so awesome"

def func_calling_func_as_first_class_obj(first_class_obj_func):
    return first_class_obj_func('bob')
