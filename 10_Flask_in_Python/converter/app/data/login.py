from converter.app.data.db.models import User, session


def log_in(login):
    """
    Login Method
    :param login:
    :return:
    """
    if session.query(User.login).filter(User.login == login).count():
        password = input('Enter password: ')
        password_user = [instance.password for instance in session.query(User.password).filter_by(login=login)]
        if password in password_user:
            return True
    else:
        print('This login or password is not found.')
        return False


