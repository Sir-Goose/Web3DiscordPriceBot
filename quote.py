from pycoingecko import CoinGeckoAPI
import web3
from web3 import Web3, HTTPProvider
import requests
import json

cg = CoinGeckoAPI()


def fetchQuoute(command, dict_from_csv):
    # split message into array to isolate token ticker
    commandArray = command.split()
    commandArray[2] = commandArray[2].lower()
    commandArray[3] = commandArray[3].lower()
    print(commandArray[2])
    print(commandArray[3])
    # print(dict_from_csv[commandArray[2]])
    quantity = commandArray[1]
    print(quantity)

    # convert ticker to token id used by coingecko
    firstTokenID = dict_from_csv[commandArray[2]]
    secondTokenID = dict_from_csv[commandArray[3]]

    # fetch respective prices
    firstTokenPrice = cg.get_price(ids=[firstTokenID], vs_currencies=['usd'])
    print("first token" + str(firstTokenPrice))
    secondTokenPrice = cg.get_price(ids=[secondTokenID], vs_currencies=['usd'])
    print("second token" + str(secondTokenPrice))

    # multiply prices by quantity
    firstTokenValue = firstTokenPrice[firstTokenID]['usd'] * float(quantity)
    print(firstTokenValue)

    # convert between tokens
    convertedValue = firstTokenValue / secondTokenPrice[secondTokenID]['usd']

    # format convertedValue
    convertedValue = "{:.4f}".format(convertedValue)
    convertedValue = "```" + str(convertedValue) + "```"



    return convertedValue
