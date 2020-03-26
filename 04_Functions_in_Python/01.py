

def my_foo(*args):
    # lst = []
    # for item in args:
    #     lst.append(item)
    #     lst.sort()
    # print(lst[-2])
    args = sorted(args)
    print(args[-2])


my_foo(2, 4, 5, 2, 3, 32, 12, 25, 98, 12, 2, 124, 23, 12, 345, 2, 23)


