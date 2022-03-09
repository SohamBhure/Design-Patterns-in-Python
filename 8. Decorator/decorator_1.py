from textwrap import wrap
from time import sleep, time
from unittest import result


def time_it(func):
    def wrapper():
        start = time()
        result = func()
        end = time()
        print(f'{func.__name__} took {int(end-start)*1000}ms')
        return result
    return wrapper

@time_it
def some_op():
    print('Starting work')
    sleep(1)
    print('Done!')
    return 401


#some_op()
#time_it(some_op)()

some_op()