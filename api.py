# Standard library imports
import time

# third-party imports
import pandas as pd
import requests
from requests.exceptions import SSLError

# customizations
pd.set_option("max_columns", 100)


def get_request(url, parameters=None):
    try:
        response = requests.get(url=url, params=parameters)
    except SSLError as s:
        print("SSL ERROR:", s)

        for i in range(5, 0, -1):
            print('\r Waiting... ({})'.format(i), end='')
            time.sleep(1)
        print('\rRetrying.' + ' '*10)

        # recursively trying again
        return get_request(url, parameters)
    if response:
        return response.json()
    else:
        # response is none usually means too many requests. Wait and try again
        print('No response, waiting 10 seconds.')
        time.sleep(10)
        print('Retrying.')
        return get_request(url, parameters)


def get_steam_data():
    url = "https://steamspy.com/api.php"
    parameters = {"request": "all"}
    json_data = get_request(url, parameters=parameters)
    steam_spy_all = pd.DataFrame.from_dict(json_data, orient='index')
    steam_spy_all.to_excel('output.xlsx', sheet_name='Steam')
