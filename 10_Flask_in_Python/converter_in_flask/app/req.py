import requests
from app import db, uri, models


def get_data_from_uri(uri):
    """
    Method for obtaining data on exchange rates from the NBRB website
    """

    response = requests.get(uri)
    currents = response.json()
    for key in currents:
        if models.Money.query.filter_by(abbreviation=key['Cur_Abbreviation']).count() == 1:
            user = models.Money.query.filter_by(abbreviation=key['Cur_Abbreviation']).first()
            user.price = key['Cur_OfficialRate']
            db.session.commit()
        else:
            new = models.Money(name=key['Cur_Name'], abbreviation=key['Cur_Abbreviation'],
                               price=key['Cur_OfficialRate'], cur_scale=key['Cur_Scale'])
            db.session.add(new)
            db.session.commit()