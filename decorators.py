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
