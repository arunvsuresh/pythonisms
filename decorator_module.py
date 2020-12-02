def demonstrate_decorator_reusability(func):
    def wrapper_for_decorator(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_for_decorator



