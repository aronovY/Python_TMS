

def seven_task(lst_svn):
    max_d = 0
    count = 0
    count_d = 0
    for i in range(0, len(lst_svn)):
        count = 0
        for item in lst_svn:
            if item == lst_svn[i]:
                count += 1
        if count > count_d:
            count_d = count
            max_d = lst_svn[i]
    print('Количество дубликатов =', count_d, ', числа', max_d, 'в списке ->', lst_svn)


v = [1, 1, 2, 1, 2]
seven_task(v)