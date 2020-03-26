

def palindrome_string(str_pal):
    if str_pal == str_pal[::-1]:
        return True
    return False


str_palin = input('Enter your string: ')
print(palindrome_string(str_palin))
