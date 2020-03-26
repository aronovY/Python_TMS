from collections import Counter


n = int(input('How many lines will be?'))
big_string = str()
for i in range(1, n + 1):
    big_string += str(input('Enter your {0} string'.format(i)))
dict_of_chars = Counter(big_string).most_common(1)
print(dict_of_chars)