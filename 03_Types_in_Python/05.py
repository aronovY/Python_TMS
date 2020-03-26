import time


start_time = time.time()
# 5
sum_of_digit = 0
for i in range(1, 20000):
    if len(str(i)) == 3:
        sum_of_digit += i
    else:
        continue
print(sum_of_digit)

# 5.1
digits = [i for i in range(1, 20000) if 99 < i < 1000]
print(sum(digits))
print("--- {0} seconds ---".format(time.time() - start_time))