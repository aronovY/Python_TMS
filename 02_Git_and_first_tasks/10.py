

def ten_task(lst_a, lst_b):
    try:
        flag_ind = None # Флаг для того что бы определять истина или лож
        for i in range(0, len(lst_a)):  # Ищем первое совпадение в списке "А"
            # Сравниваем элементы списка "А" с первым элементом списка "B"
            if lst_a[i] != lst_b[0]:
                continue
            elif lst_a[i] == lst_b[0]:  # Если элементы равны переходим в этот блок
                ind = i
                for item in lst_b:
                    if ind < len(lst_a):
                        if item == lst_a[ind]:
                            ind += 1
                            flag_ind = True
                        else:
                            flag_ind = False
                            break
                    else:
                        flag_ind = False
                        break
                if flag_ind:
                    break
        if flag_ind:
            print('Список {0}, является подмасивом списка {1}'.format(lst_b, lst_a))
        else:
            print('Список {0}, не является подмасивом списка {1}'.format(lst_b[:], lst_a[:]))
    except IndexError as exc:
        print('Exception ->', exc)


lst_1 = [1, 2, 3, 5, 8, 5, 8, 3, 13, 42, 5, 8]
lst_2 = [5, 8, 3]
ten_task(lst_1, lst_2)