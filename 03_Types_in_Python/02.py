import itertools


# 2.0
def lst_compil(lst_1):
    new_lst = tuple(itertools.combinations(lst_1, 2))
    print('This list {0} -> {1}'.format(lst_1, new_lst))


lst = [72, 586, 12, 1]
lst_compil(lst)


# 2.1
# lst = [72, 586, 12, 1]
# new_list = []
# new_list.append(72)
# new_list.append(586)
# new_list.append(12)
# print(tuple(new_list))
