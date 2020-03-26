import re


domains = ['baveja@att.net', 'mhassel@comcast.net', 'heine@sbcglobal.net', 'gbacon@comcast.net', 'slaff@hotmail.com',
          'seemant@yahoo.com', 'miltchev@verizon.net', 'ducasse@hotmail.com', 'chaikin@yahoo.ca', 'agolomsh@yahoo.ca', 'joehall@msn.com', 'ilikered@optonline.net']


def domain_for_string(dom):
    for item in dom:
        for lit in range(len(item)):
            if item[lit] == '@':
                start = lit
            elif item[lit] == '.':
                finish = lit
        print(item[start:finish], end=', ')


def domain_for_regular(dom):
    for item in dom:
        print(re.findall(r'@\w+', item), end=', ')


domain_for_regular(domains)
#domain_for_string(domains)



