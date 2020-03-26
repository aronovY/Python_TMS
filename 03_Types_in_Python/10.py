lst_of_lst = [[2, 12], [23, 21], [5, 32], [14, 19], [31, 8]]
lst_of_lst.sort(key=lambda x: sum(x), reverse=True)
print(lst_of_lst)
