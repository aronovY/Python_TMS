

def counter_letters(str_hw):
    count_low = 0
    count_up = 0
    count_sp = 0
    count_punct = 0
    for letter in str_h:
        if 'a' <= letter <= 'z':
            count_low += 1
        elif 'A' <= letter <= 'Z':
            count_up += 1
        elif letter == ' ':
            count_sp += 1
        elif letter in '!?,.-':
            count_punct += 1
    print('In {0}: upper letter: {1}, lower letter: {2}, space: {3}, punctuation: {4}'.format(str_hw, count_up,
                                                                                              count_low, count_sp,
                                                                                              count_punct))


str_h = 'Hello, World!!'
counter_letters(str_h)