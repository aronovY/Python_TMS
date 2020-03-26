

def calculate_chars(string):
    counter = []
    pare = []
    for i in range(len(string)):
        count = 0
        if string[i].lower() not in counter:
            counter += string[i].lower()
            for y in range(len(string)):
                if string[y].lower() == string[i].lower():
                    count += 1
            pare.append(count)
        else:
            continue
    words = dict(zip(counter, pare))
    print('Numbers litters in string: "{}" >>> {}'.format(string, words))


a = 'Hello my dear friend!!!'
calculate_chars(a)