import datetime
import numpy


def five_task(f_d, s_d):
    f_d = f_d.split('_')
    s_d = s_d.split('_')
    start_date = datetime.date(int(f_d[0]), int(f_d[1]), int(f_d[2]))
    end_date = datetime.date(int(s_d[0]), int(s_d[1]), int(s_d[2]) + 1)
    print('Рабочие дни с', start_date, 'по', end_date, 'включая эти дни ->', numpy.busday_count(start_date, end_date))


first_date = '2019_7_2'
second_date = '2019_7_11'
five_task(first_date, second_date)