

def sum_rec(i):
    if i == 0:
        return i
    return i + sum_rec(i - 1)


print(sum_rec(4))
