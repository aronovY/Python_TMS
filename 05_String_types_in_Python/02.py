import re


def split_word_with_method(str_m):
    str_m = ''.join([symbol for symbol in str_m if symbol not in ('!', '?', ',', '.', '-')])
    for i in str_m.split():
        if len(i) < 3:
            if len(i) == 2:
                print(i + ' ', end=' ')
            elif len(i) == 1:
                print(i + '  ', end=' ')
        else:
            print(i[:3], end=' ')


def split_word_with_regular(str_re):
    str_re = ''.join([symbol for symbol in str_re if symbol not in ('!', '?', ',', '.', '-')])
    for i in str_re.split():
        if len(i) == 2:
            print((re.findall(r'^.{0,3}', i + ' ')))
        elif len(i) == 1:
            print((re.findall(r'^.{0,3}', i + '  ')))
        else:
            print((re.findall(r'^.{0,3}', i)))


srt_me = 'Hello! mY dihxr fr-en s kkfjn wa'
split_word_with_method(srt_me)
print()
split_word_with_regular(srt_me)
