

def pro_list(lst_el, i):
    # if i >= len(lst_el):
    #     return lst_el[len(lst_el) - 1]
    # return lst_el[i] * pro_list(lst_el, i + 1)
    if i == 0:
        return lst_el[0]
    else:
        return lst_el[i] * pro_list(lst_el, i - 1)


lst = [42, 72, 113]
print(pro_list(lst, len(lst) - 1))