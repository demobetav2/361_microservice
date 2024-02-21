# Darrell Thompson
# CS 361
# Microservice

import sys
import requests

def fetchExchangeRate(base_currency: str, target_currency: str) -> str:
    """
    Provides currency conversion rate between two currencies from exchangerate-api.com

    :param base_currency (str): currency to convert from, i.e. USD, GBP, YEN

    :param target_currency (str): currency to convert to, i.e. USD, GBP, YEN

    :return (str): Currency conversion rate if request was successful, otherwise error response
    """
    exchange_api = f'https://v6.exchangerate-api.com/v6/824942133be5e6a30af37374/pair/{base_currency}/{target_currency}'

    try:
        response = requests.get(exchange_api)
        response.raise_for_status()             # Check for API connection error
        data = response.json()                  # Valid API response

        # If valid, print conversion rate
        if data['result'] == 'success':
            print(data['result'], data['conversion_rate'])

        # If unsuccessful, print API error status
        else:
            print(f'API request response: {data['result']}')

    # If connection error
    except requests.RequestException as error:
        print(f'API request error: {error}')


fetchExchangeRate(sys.argv[1], sys.argv[2])
