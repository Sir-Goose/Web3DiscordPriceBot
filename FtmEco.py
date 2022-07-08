import discord
import os
import requests
import json

import web3
from web3 import Web3, HTTPProvider


def get_boo_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=spookyswap&vs_currencies=usd')
    json_data = json.loads(response.text)
    booPrice = json_data['spookyswap']['usd']
    booPrice = round(booPrice, 2)

    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=spookyswap&vs_currencies=usd&include_24hr_change=true')
    json_data = json.loads(response.text)
    booChange = json_data['spookyswap']['usd_24h_change']
    booChange = round(booChange, 2)

    booPrice = "```" + "BOO $" + str(booPrice) + " (" + str(booChange) + "%" + " 24h" + ")" + "```"

    return booPrice

def get_crv_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=curve-dao-token&vs_currencies=usd')
    json_data = json.loads(response.text)
    crvPrice = json_data['curve-dao-token']['usd']
    crvPrice = round(crvPrice, 2)

    response = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=curve-dao-token&vs_currencies=usd&include_24hr_change=true')
    json_data = json.loads(response.text)
    crvChange = json_data['curve-dao-token']['usd_24h_change']
    crvChange = round(crvChange, 2)

    crvPrice = "```" + "CRV $" + str(crvPrice) + " (" + str(crvChange) + "%" + " 24h" + ")" + "```"

    return crvPrice

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



