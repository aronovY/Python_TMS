

def roman_to_int(roman):
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rule_digits = {('I', 'V'): 3, ('I', 'X'): 8, ('X', 'L'): 30, ('X', 'C'): 80, ('C', 'D'): 300, ('C', 'M'): 800}
    arab = 0
    prev_lit = None
    for lit in roman:
        if prev_lit and digits[prev_lit] < digits[lit]:
            arab += rule_digits[(prev_lit, lit)]
        else:
            arab += digits[lit]
        prev_lit = lit
    print('Roman number {} >>> {}'.format(roman, arab))


# roman_to_int('I')
# roman_to_int('II')
# roman_to_int('III')
# roman_to_int('IV')
# roman_to_int('V')
# roman_to_int('VI')
roman_to_int('IX')
# roman_to_int('VIII')
# roman_to_int('IX')
# roman_to_int('X')
# roman_to_int('CXI')