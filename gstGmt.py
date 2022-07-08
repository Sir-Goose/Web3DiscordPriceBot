import discord
import os
import requests
import json

import web3
from web3 import Web3, HTTPProvider


def get_gst_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=green-satoshi-token&vs_currencies=usd')
    json_data = json.loads(response.text)
    gstPrice = json_data['green-satoshi-token']['usd']
    gstPrice = round(gstPrice, 2)

    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=green-satoshi-token&vs_currencies=usd&include_24hr_change=true')
    json_data = json.loads(response.text)
    gstChange = json_data['green-satoshi-token']['usd_24h_change']
    gstChange = round(gstChange, 2)

    gstPrice = "```" + "GST $" + str(gstPrice) + " (" + str(gstChange) + "%" + " 24h" + ")" + "```"

    return gstPrice

def get_gmt_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=stepn&vs_currencies=usd')
    json_data = json.loads(response.text)
    gmtPrice = json_data['stepn']['usd']
    gmtPrice = round(gmtPrice, 2)

    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=stepn&vs_currencies=usd&include_24hr_change=true')
    json_data = json.loads(response.text)
    gmtChange = json_data['stepn']['usd_24h_change']
    gmtChange = round(gmtChange, 2)

    gmtPrice = "```" + "GMT $" + str(gmtPrice) + " (" + str(gmtChange) + "%" + " 24h" + ")" + "```"

    return gmtPrice


