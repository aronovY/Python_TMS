import datetime
import re


def date_in_text(string):
    date = re.findall(r'((0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-[12]\d{3})', string)
    print(date)


text = "Lorem ipsum dolor sit Amit 34-3456 12-06-2012 amet, consectetur adipiscing elit, sed do eiusmod tempor Amit " \
       "42-2216 31-06-2019 incididunt ut labore et dolore Amit 32-6782 03-12-2270 magna aliqua."
date_in_text(text)