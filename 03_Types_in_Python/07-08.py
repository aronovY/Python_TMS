from string import ascii_letters
from random import choice
import random


# 7
lst_of_letters = []
rnd = random.randint(1, 4)
rng = int(input('Enter your size of list: '))
for i in range(rng):
    lst_of_letters.append(''.join(choice(ascii_letters) for ind in range(rnd)))
print(lst_of_letters)

# 8
second_lst_of_letters = []
for item in lst_of_letters:
    second_lst_of_letters.append(item[::-1])
print((sorted(second_lst_of_letters, key=str.lower(), reverse=True)))