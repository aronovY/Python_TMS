digits = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
          'nine': 9}

digits_tens = {'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
               'seventeen': 17, 'eighteen': 18, 'nineteen': 19}

digits_to_hundred = {'twenty': 20, 'thirsty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
                     'eighty': 80, 'ninety': 90, 'hundred': 100}

operations = {'plus': '+', 'minus': '-', 'multiply': '*', 'div': '/'}


def update_lst(lst_value, value, item):
    """
    We delete the operands and the operation after execution,
    and add the resulting answer to the list after the operation is completed
    """

    lst_value[item - 1] = value
    del (lst_value[item + 1], lst_value[item])


def checkout_operations(lst):
    """
    Checking the correctness of the expression, the length of the tuple should be odd.

    Every second list item must be an operator, otherwise the expression is not true.
    """

    if len(lst) % 2 != 0:
        for ar in lst[1::2]:
            if ar in operations.keys():
                continue
            else:
                return False
        return True


def digits_word(*args):
    lst_value = []
    if checkout_operations(args):
        for arg in args:  # In this loop, create an expression with a list
            if arg.split()[0] in digits_to_hundred.keys():
                if len(arg.split()) > 1:
                    lst_value.append(digits_to_hundred[arg.split()[0]] + digits[arg.split()[1]])
                else:
                    lst_value.append(digits_to_hundred[arg])
            elif arg in digits.keys():
                lst_value.append(digits[arg])
            elif arg in digits_tens.keys():
                lst_value.append(digits_tens[arg])
            else:
                lst_value.append(operations[arg])

        while '*' in lst_value or '/' in lst_value:  # While there is multiplication or division in the list, we solve them first
            print(lst_value)
            for item in range(len(lst_value) - 1):
                if '*' == lst_value[item]:
                    value = int(lst_value[item - 1] * lst_value[item + 1])
                    update_lst(lst_value, value, item)
                    break
                elif '/' == lst_value[item]:
                    value = int(lst_value[item - 1] / lst_value[item + 1])
                    update_lst(lst_value, value, item)
                    break

        while '+' in lst_value or '-' in lst_value:  # While the list has a plus or minus
            print(lst_value)
            for item in range(len(lst_value) - 1):
                if '+' == lst_value[item]:
                    value = int(lst_value[item - 1] + lst_value[item + 1])
                    update_lst(lst_value, value, item)
                    break
                elif '-' == lst_value[item]:
                    value = int(lst_value[item - 1] - lst_value[item + 1])
                    update_lst(lst_value, value, item)
                    break
        return lst_value

    else:
        return 'Bad value'


su = digits_word('hundred', 'div', 'five', 'plus', 'forty nine', 'minus', 'thirsty', 'multiply', 'five')
print('Your answer ->', su)
