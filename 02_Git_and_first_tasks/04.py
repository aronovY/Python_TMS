

def four_task(year, month):
    c = calendar.TextCalendar(0)
    print(c.formatmonth(year, month))


four_task(int(input('Введите год: ')), int(input('Введите месяц: ')))