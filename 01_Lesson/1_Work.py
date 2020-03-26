import math
import os


def to_fixed(num_obj, digits = 0):
    return f"{num_obj:.{digits}f}"


def one():
    try:
        first_value = float(input('Input first number: '))
        second_value = float(input('Input second number: '))
        sum_of_values= first_value + second_value
        difference = first_value - second_value
        print('Sum -> ', int(sum_of_values))
        print('Difference -> ', difference)
        print('Sum of two new value -> ', sum_of_values + difference)
    except ValueError as exc:
        print('Exception,', exc)
    else:
        print('Try again!')


def two(value_two):
    if value_two % 2 == 0 and 2 <= value_two <= 27:
        print('In first range')
    elif value % 2 == 0:
        print('Odd')
    elif value_two % 2 != 0 and 29 <= value_two <= 53:
        print('In second range')
    else:
        print('It\'s something')


def four(str_out):
    count_symbol = 0
    str_without_prob = str()
    for words in str_out.split():
        count_symbol += len(words)
        if count_symbol > 20:
            count_symbol = 0
            str_without_prob += words
            str_without_prob += '\n\t'
        elif count_symbol == 20:
            str_without_prob += words
            str_without_prob += '\n\t'
            count_symbol = 0
        elif count_symbol < 20:
            str_without_prob += words
    print(str_without_prob)


def five(quantity, lst_f):
    new_lst = []
    for i in lst_f:
        if isinstance(i, str):
            del i
        elif isinstance(i, float):
            new_lst.append(int(i))
        else:
            new_lst.append(i)
    new_lst.sort()
    print(new_lst[:quantity])


def eight(ls_f_dig):
    new_lst = ls_f_dig
    while len(new_lst) > 1:
        if len(new_lst) == 2:
            del new_lst[1]
            break
        elif len(new_lst) % 2 != 0:
            del new_lst[1::2]
            del new_lst[0]
        elif len(new_lst) % 2 == 0:
            del new_lst[1::2]
    print(new_lst)


def nine(frst, scnd, rslt):
    flag_n = True
    summ = 0
    print(frst, scnd)
    while flag_n:
        if frst + scnd < rslt:
            summ = frst + scnd
            frst = scnd
            scnd = summ
            print(summ, end=', ')
            continue
        elif frst + scnd == rslt:
            print('It\'s true')
            print(rslt)
            break
        elif frst + scnd > rslt:
            print('It\'s false')
            break
        


flag = True

while flag:
    os.system('clear')
    print('1. Программа принимает на входе два числа. Выводит первой строкой - их сумму в целочисленном виде, второй '
          'строкой - из разность, третей строкой - сумму двух новых чисел.')
    print('2. Программа получает на  входе число и выводит слово "Odd" если число четное.'
          ' Если число четное и в диапазоне от 2 до 27, то выводит "In first range", если число нечетное и в диапазоне '
          'от 29 до 53, то выводит "In second range", во всех других случаях "It\'s something".')
    print('3. Программа принимает на входе два числа и выводит первой строкой '
          'целочисленное частное этих двух чисел (округлить всегда в меньшую сторону), второй строкой - '
          'дробное частное.')
    print('4. Программа, которая на входе будет принимает строку, '
          'а выводит ее на экран первые двадцать символов (если эта длинна разрывает слово, '
          'то печатает слово целиком), затем продолжает на новой строке и делает 4 отступа вначале '
          'и снова двадцать символов.')
    print('5. Программа, которая принимает в качестве первого аргумента число — '
          'количество необходимых результатов, второго - список чисел. Программа ищет переданное в качестве '
          'первого количество результатов с наиболее высокими показателями из переданного в качестве второго аргумента'
          ' списка.')
    print('6. Программа, которая принимает на входе радиус и выводит на экран площадь круга.')
    print('7. Программа, которая принимает две строки и выводит на печать их в обратном порядке в')
    print('8. Программа, которая в качестве первого аргумента принимает список упорядоченных '
          'уникальных чисел. С каждым циклом каждое число исключает соседа и передает "право исключения" следующему '
          'числу по принципу: список - [1, 2, 3, 4, 5, 6]. 1 исключает 2, 2 пропускается, так как исключено. '
          '3 исключает 4, 5 исключает 6 - цикл закончен и так до тех пор, пока не останется одно число. ')
    print('*9. Необходимо написать программу, которая в качестве первого аргумента принимает три числа. '
          'Из первых двух генерирует последовательность чисел, в которой каждое последующее число равно сумме двух '
          'предыдущих и проверяет, входит ли третье число в этот ряд.')
    print('0. EXIT!')

    value = input('Enter your choice: ')

    if int(value) == 1:  # Задание 1.
        one()
        input()
    elif int(value) == 2:  # Задание 2.
        dig = int(input('Enter your value: '))
        two(dig)
        input()
    elif int(value) == 3:  # Задание 3.
        try:
            a = input('Enter first value: ')
            b = input('Enter second value: ')
            if a.isdigit() and b.isdigit():
                print(int(a / b))
                print(round(float(a / b)))
        except ZeroDivisionError as e:
            print('Exception,', e)
        except ValueError as ee:
            print('Exception,', ee)
        input()
    elif int(value) == 4:
        str_my = input('Enter your string: ')
        four(str_my)
        input()
    elif int(value) == 5:  # Задание 5.
        kol = int(input('Enter your number of digits: '))
        lst = [20, 58, 'string', 23, 62, 6.45, 48, 55, 95, 68, 2, 2, 50, 76, 14, 92, 12, 71, 12, 30]
        five(kol, lst)
        input()
    elif int(value) == 6:  # Задание 6.
        radius = float(input('Enter radius: '))
        S = math.pi * radius ** 2
        print('Area of a circle =', to_fixed(S, 3))
        input()
    elif int(value) == 7:  # Задание 7.
        first_string = str(input('First string: '))
        second_string = str(input('Second string: '))
        print(second_string[::-1].lower(), ',', first_string[::-1].lower())
        input()
    elif int(value) == 8:  # Задание 8.
        lst_for_digits = [1, 2, 3, 4, 5, 6]
        eight(lst_for_digits)
        input()
    elif int(value) == 9:  # Задание 9 со звездочкой
        first = int(input('Enter first number: '))
        second = int(input('Enter second number: '))
        result = int(input('Enter result: '))
        nine(first, second, result)
        input()
    elif int(value) == 0:
        flag = False
    else:
        print('Enter correct input. \nTRY AGAIN.')
        input()


