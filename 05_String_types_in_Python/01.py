import re


def return_string_for_method(str_s):
    word = str_s.split()[:1]
    print('First word with method:', word[0])  # or str_s.split()[:1])


def return_string_for_regular(str_re):
    print(re.findall(r'\w+', str_re)[0])


return_string_for_method(input('Enter your string (string method: '))
return_string_for_regular(input('Enter your string (regular):'))
