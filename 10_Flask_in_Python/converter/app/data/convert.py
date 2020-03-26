
from app.data.calculate import calculation


def convert_data(cur, userid):
    """
    Method for filtering and selecting a specific user currency
    :param cur:  # list of currencies we work with
    """
    flag = True
    while flag:
        for key in cur:
            print(f"{key['Abbreviation']} - {key['Name']}")
        f_cur = input('\nChoose currency: ')
        s_cur = input('\nChoose the currency to which to transfer: ')
        for key in cur:
            if f_cur.upper() in key['Abbreviation']:
                flag = True
                break
            elif f_cur.upper() == 'BYN':
                flag = True
                break
            else:
                flag = False
                continue

        if flag:
            for key in cur:
                if s_cur.upper() in key['Abbreviation']:
                    flag = True
                    break
                elif s_cur.upper() == 'BYN':
                    flag = True
                    break
                else:
                    flag = False
                    continue

        if flag:
            money = int(input(f'How much to convert from {f_cur.upper()} to {s_cur.upper()}?\n'))
            print(calculation(f_cur, s_cur, money, cur, userid))
            input('Press Enter')
            flag = False
        else:
            print('Try one more')
