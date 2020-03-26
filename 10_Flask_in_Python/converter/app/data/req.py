import requests


def get_data_from_uri(uri):

    """
    Method for obtaining data on exchange rates from the NBRB website
    """
    
    response = requests.get(uri)
    currents = response.json()
    return [{'Abbreviation': key['Cur_Abbreviation'], 'Name': key['Cur_Name'],
            'How many units': key['Cur_Scale'], 'BYN': key['Cur_OfficialRate']}
            for key in currents]

