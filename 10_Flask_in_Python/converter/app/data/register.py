from app.data.db.models import User, session


def registration():
    """
    Method for registering new users
    """

    new_name = input('Enter your name: ')
    new_surname = input('Enter your surname: ')
    new_login = input('Enter your login: ')
    new_password = input('Enter your password: ')
    print()
    if session.query(User.login).filter(User.login != new_login).count() == 1:
        session.add(User(new_name, new_surname, new_login, new_password))
        session.commit()

    else:
        print('This username is being used by another user.')
