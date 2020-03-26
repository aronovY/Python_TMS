

def third_task(n):
    first_number = str(n)
    second_number = str(n + n)
    third_number = str(n + n + n)
    four_number = str(n + n + n + n)
    print(first_number,'+',second_number, '+', third_number, '+', four_number,'=',
          int(first_number) + int(second_number) - int(third_number) * int(four_number))


third_task(input('Enter your number'))