from app import db
from app.models import Money, History


def calculation(first_cur, how_m, second_cur, user_id):
    """
    Method for working with transferred data for currency calculation
    :param first_cur:  # first abbreviation
    :param second_cur: # second abbreviation
    :param how_m: # transfer amount
    :param user_id: # Id of user
    :return: # get the answer
    """

    first = Money.query.filter_by(abbreviation=first_cur).first()
    second_money = Money.query.filter_by(abbreviation=second_cur).first()

    # Based on if the first currency BYN
    if first_cur.upper() == 'BYN':
        total = round(how_m / second_money.price * second_money.cur_scale, 2)

    # Based on if the second currency BYN
    elif second_cur.upper() == 'BYN':
        total = round(first.price / first.cur_scale * how_m, 2)

    else:
        total = round(first.price / first.cur_scale * how_m / (second_money.price / second_money.cur_scale), 2)

    history = History(first_currency=first_cur.upper(),
                      how_much=how_m,
                      second_currency=second_cur.upper(),
                      total=total,
                      user_id=user_id)
    db.session.add(history)
    db.session.commit()

    return total
