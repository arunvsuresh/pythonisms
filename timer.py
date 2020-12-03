import timeit


def timer_decorator(func):

    def wrapper_for_timer_decorator(*args):
        st_time = timeit.default_timer()
        func(*args)
        end_time = timeit.default_timer()
        runtime = end_time - st_time
        return 'runtime: ', runtime
    return wrapper_for_timer_decorator

