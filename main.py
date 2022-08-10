import discord
import os
import requests
import json

import csv

import FtmEco
import deiDeus
import anyPrice
import gstGmt
import colorTest
import historicalPrice
import quote

client = discord.Client()

dict_from_csv = {}
# convert csv to dictionary
with open('cgtokens.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]: rows[1] for rows in reader}

print("csv loaded")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # List servers bot is in
    activeServers = client.guilds
    print(activeServers)


@client.event
async def on_message(message):
    with open("messages.txt", "a") as external_file:
        add_text = message.content
        print(add_text, file=external_file)
        external_file.close()

    if message.author == client.user:
        return

    if message.content.startswith('$p'):
        command = message.content
        tokenFormattedPrice = anyPrice.get_any_price(command, dict_from_csv)

        await message.channel.send(tokenFormattedPrice, reference=message)

    if message.content.startswith('$h'):
        command = message.content
        historicalFormattedPrice = historicalPrice.get_historical_price(command, dict_from_csv)
        await message.channel.send(historicalFormattedPrice, reference=message)

    if message.content.startswith('$convert'):
        command = message.content
        convertedValue = quote.fetchQuoute(command, dict_from_csv)
        await message.channel.send(convertedValue, reference=message)

    #if message.content.startswith('$tokens'):
        #trackedCoins = "```" + "imp\nimp\ngst\ngmt\ndei\ndeus\nboo\crv" + "```"
        #await message.channel.send(trackedCoins)

    if message.content.startswith('$request'):
        with open("requests.txt", "a") as external_file:
            add_text = message.content
            print(add_text, file=external_file)
            external_file.close()
        await message.channel.send("**Received**", reference=message)
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)

    if message.content.startswith('$imp'):
        command = message.content
        command = "$p imp"
        tokenFormattedPrice = anyPrice.get_any_price(command, dict_from_csv)
        await message.channel.send(tokenFormattedPrice, reference=message)

    if message.content.startswith('$IMP'):
        command = message.content
        command = "$p imp"
        tokenFormattedPrice = anyPrice.get_any_price(command, dict_from_csv)
        await message.channel.send(tokenFormattedPrice, reference=message)

    if message.content.startswith('$deus'):
        deusPrice = deiDeus.get_deus_price()
        await message.channel.send(deusPrice, reference=message)

    if message.content.startswith('$dei'):
        deiPrice = deiDeus.get_dei_price()
        await message.channel.send(deiPrice, reference=message)

    if message.content.startswith('$gst'):
        gstPrice = gstGmt.get_gst_price()
        await message.channel.send(gstPrice, reference=message)

    if message.content.startswith('$gmt'):
        gmtPrice = gstGmt.get_gmt_price()
        await message.channel.send(gmtPrice, reference=message)

    #if message.content.startswith('$colortext'):
        #colortextexample = colorTest.color_test()
        #await message.channel.send(colortextexample, reference=message)

    if message.content.startswith('$boo'):
        booPrice = FtmEco.get_boo_price()
        await message.channel.send(booPrice, reference=message)

    if message.content.startswith('$crv'):
        crvPrice = FtmEco.get_crv_price()
        await message.channel.send(crvPrice, reference=message)

    words = message.content
    print(words)
    words = words.split()
    length = len(words)
    i = 0
    while i < length:
        if words[i] == 'meta':
            await message.channel.send("Did you mean Facebook?", reference=message)
        i = i + 1

client.run('')
