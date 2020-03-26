import http

import requests
import os
import pandas
from app.data import convert
from app.data import req
from app.data.login import log_in
from app.data.register import registration
from app.data.db.models import User, session


# We store in a constant variable a link to the exchange rates of the NBRB website

uri = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'


def menu():
    """
    Interactive program menu for working with the user.
    """

    if requests.get(uri).status_code == http.HTTPStatus.OK:
        main_menu = req.get_data_from_uri(uri)
        flag_1 = True
        while flag_1:
            try:
                os.system('clear')
                inter_menu = int(input('\t\t\t===CONVERTER==='
                                       '\n\t\t1. Register'
                                       '\n\t\t2. Login'
                                       '\n\t\t3. Exit\n'))
                if inter_menu == 1:
                    os.system('clear')
                    registration()
                elif inter_menu == 2:
                    os.system('clear')
                    login = input('Enter login: ')
                    flag_2 = log_in(login)
                    user_id = [instance.id for instance in session.query(User.id).filter_by(login=login)]
                    if flag_2:
                        while flag_2:
                            os.system('clear')
                            value = int(input(f'\t\t\tWELCOME {login}!!!\t\t\t\n'
                                              f'\tThis is a currency converter program\n'
                                              f'Select an action:\n'
                                              f'1: List of all currencies\n'
                                              f'2: Converter currencies\n'
                                              f'3: Exit\n'))
                            if value == 1:
                                print(pandas.DataFrame(main_menu))
                                input('Press Enter')
                            elif value == 2:
                                os.system('clear')
                                convert.convert_data(main_menu, user_id)
                                input()
                            elif value == 3:
                                os.system('clear')
                                print('Goodbye')
                                flag_2 = False
                                os.system('clear')
                            else:
                                print('Repeat Entry')
                                print()
                else:
                    flag_1 = False
            except ValueError:
                print('Repeat Entry')
                os.system('clear')



