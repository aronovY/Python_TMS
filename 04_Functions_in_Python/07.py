import math


def is_prime(value):
    for i in range(2, int(math.sqrt(value) + 1)):
        if value % i == 0:
            return False
    return value > 1


number = int(input('Enter your number: '))
print(is_prime(number))