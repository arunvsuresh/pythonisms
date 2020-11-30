def func1(name):
    return f"hello {name}"

def func2(name):
    return f"{name}, you're so awesome"

# passing in functions to other functions
def func_calling_func_as_first_class_obj(*args):
    for func in args:
        print(func('arun'))

    # result of passing func1 & func2 into func_calling_func_as_first_class_obj:
    # func_calling_func_as_first_class_obj(func1, func2)
    # output:
    # hello arun
    # arun, you're so awesome

# assigning func to variable to be used later on
def func_acting_as_variable(text=None):
    def greet(text):
        return text.upper() + "!"

    var = greet
    if text is None:
        return var('text')
    else:
        return var(text)


# passing in functions to a list
def func_in_data_structures(*args):
    lst = [arg for arg in args]
    return lst

# demonstrate how python functions can capture local state
def functions_capturing_local_state(a):
    def add(b):
        return a + b
    return add

def call_functions_capturing_local_state():
    adder = functions_capturing_local_state(4)
    return adder(5)
