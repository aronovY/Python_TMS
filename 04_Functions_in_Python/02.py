

def func(a_2, b_2):
    flag = False
    if a_2 in b_2.values():
        flag = True
        print(flag)
    else:
        print(flag)


a = 8
b = {'foo': 2, 'bar': 8}
func(a, b)
