

def sum_of_digits_word(*args):
    su = 0
    digits = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
              'six': 6, 'seven': 7, 'eight': 8,
              'nine': 9, 'ten': 10}
    print(sum([digits[arg.lower()] for arg in args if arg in digits]))


sum_of_digits_word('Zero', 'One', 'Two', 'THREE', 'four', 'fIvE', 'sIx', 'SeVen', 'EIGht', 'NIne', 'tEN')
