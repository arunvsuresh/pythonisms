from decorator_module import demonstrate_decorator_reusability
from timer import timer_decorator

# demonstrate underlying behavior of decorators
def my_decorator(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper


def hello():
    print('hello')


hello = my_decorator(hello)
hello()

# adding some syntactic sugar
def syntactic_sugar_decorator(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper


@syntactic_sugar_decorator
def hi():
    print('hi')


@demonstrate_decorator_reusability
def greeting(name):
    return f"greeting! {name}"


@timer_decorator
def operations(*args):
    if len(args) == 1:
        return sum([i for i in range(args[0])])


print(operations(10000))
