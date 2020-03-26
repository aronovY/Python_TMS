import re


def convert_words(string):
    print(string, '-> ', end='')
    for item in string:
        if str.islower(item):
            print(item.upper(), end='')
        elif str.isupper(item):
            print(item.lower(), end='')
        else:
            print(item, end='')


string_reverce = 'hELLO WORLD'
convert_words(string_reverce)
