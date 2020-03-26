

def replace_char(string, index, char):
    string = string[:index] + char + string[index + 1:]
    print(string)


replace_char('Hello World!', 5, 'b')