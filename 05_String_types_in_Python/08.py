

def palindrome(string):
    string_b = string[::-1]
    print("True" if string.replace(' ', '').lower() == string_b.replace(' ', '').lower() else "False")


palindrome('Never odd or even')