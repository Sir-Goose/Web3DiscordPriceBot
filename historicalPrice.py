from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def get_historical_price(command, dict_from_csv):
    commandArray = command.split()
    tokenId = dict_from_csv[commandArray[1]]
    tokenId = tokenId.lower()

    date = commandArray[2]
    print(date)

    historicalPrice = cg.get_coin_history_by_id(id=tokenId, date=str(date), localization='false')
    historicalPrice = historicalPrice['market_data']['current_price']['usd']
    historicalPrice = round(historicalPrice, 2)
    print(historicalPrice)
    historicalPrice = "```" + tokenId + " $" + str(historicalPrice) + " at " + date + "```"
    historicalFormattedPrice = historicalPrice

    return historicalFormattedPrice
