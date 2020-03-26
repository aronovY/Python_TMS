

def nine_task(lst_n):
    for i in range(0, len(lst_n)):
        if lst_n[i] == 237:
            for item in lst_n[i:]:
                if int(item) % 2 == 0:
                    print(item, end=', ')
                else:
                    continue


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237,
           412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843,
           831, 445, 742, 717, 958, 743, 527]

nine_task(numbers)