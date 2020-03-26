import random
import bisect


start = int(input('Enter start random: '))
end = int(input('Enter End random: '))
lst_of_digits = [random.randint(start, end) for i in range(5, 10)]
lst_of_digits.sort()
new_dig = [random.randint(start, end) for i in range(5)]
for item in new_dig:
    print('This digit {0} in this list -> {1}'.format(item, lst_of_digits))
    bisect.insort(lst_of_digits, item)
print('New list with all digit -> {0}'.format(lst_of_digits))
