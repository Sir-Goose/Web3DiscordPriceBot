import discord
import os
import requests
import json

import web3
from web3 import Web3, HTTPProvider


def get_deus_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=deus-finance-2&vs_currencies=usd')
    json_data = json.loads(response.text)
    deusPrice = json_data['deus-finance-2']['usd']
    deusPrice = round(deusPrice, 2)

    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=deus-finance-2&vs_currencies=usd&include_24hr_change=true')
    json_data = json.loads(response.text)
    deusChange = json_data['deus-finance-2']['usd_24h_change']
    deusChange = round(deusChange, 2)

    deusPrice = "```" + "DEUS $" + str(deusPrice) + " (" + str(deusChange) + "%" + " 24h" + ")" + "```"

    return deusPrice

def get_dei_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=dei-token&vs_currencies=usd')
    json_data = json.loads(response.text)
    deiPrice = json_data['dei-token']['usd']
    deiPrice = round(deiPrice, 2)

    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=dei-token&vs_currencies=usd&include_24hr_change=true')
    json_data = json.loads(response.text)
    deiChange = json_data['dei-token']['usd_24h_change']
    deiChange = round(deiChange, 2)

    deiPrice = "```" + "DEI $" + str(deiPrice) + " (" + str(deiChange) + "%" + " 24h" + ")" + "```"

    return deiPrice