from copy import deepcopy

x = {'a': 1, 'b': {'c': 1}}
# y = x
# y['a'] = 2
# y['b']['c'] = 5
# print(x)
# z = x.copy()
y = deepcopy(x)
y['a'] = 2
y['b']['c'] = 5
print(x)