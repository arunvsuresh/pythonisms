def demonstrate_decorator_reusability(func):
    def wrapper_for_decorator():
        func()
        func()
    return wrapper_for_decorator



