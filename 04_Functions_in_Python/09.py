import time


def decorator(func):
    def wrapper_func(arg1, arg2):
        start_time = time.time()
        func(arg1, arg2)
        print('Program execution time:', time.time() - start_time)
    return wrapper_func


@decorator
def foo(a_2, b_2):
    flag = False
    for values in b_2:
        if a_2 == b_2[values]:
            flag = True
            break
    if flag:
        print(flag)
    else:
        print(flag)


a = 5
b = {'foo': 5, 'bar': 8}
foo(a, b)
