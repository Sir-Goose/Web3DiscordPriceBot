import time

import discord
import os
import requests
import json

import csv

from discord.ext.commands import bot

import FtmEco
import deiDeus
import anyPrice
import gstGmt
import colorTest
import historicalPrice
import quote
import statusUpdater

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

    if message.author == client.user:
        return

    if message.content.startswith('$p'):
        command = message.content
        tokenFormattedPrice = anyPrice.get_any_price(command, dict_from_csv)

        await message.channel.send(tokenFormattedPrice)

    if message.content.startswith('$h'):
        command = message.content
        historicalFormattedPrice = historicalPrice.get_historical_price(command, dict_from_csv)
        await message.channel.send(historicalFormattedPrice)

    if message.content.startswith('$convert'):
        command = message.content
        convertedValue = quote.fetchQuoute(command, dict_from_csv)
        await message.channel.send(convertedValue)

    if message.content.startswith('$tokens'):
        trackedCoins = "```" + "imp\nimp\ngst\ngmt\ndei\ndeus\nboo\crv" + "```"
        await message.channel.send(trackedCoins)

    if message.content.startswith('$request'):
        with open("requests.txt", "a") as external_file:
            add_text = message.content
            print(add_text, file=external_file)
            external_file.close()
        await message.channel.send("**Received**")

    if message.content.startswith('$imp'):
        command = message.content
        tokenFormattedPrice = anyPrice.get_any_price(command, dict_from_csv)
        await message.channel.send(tokenFormattedPrice)

    if message.content.startswith('$IMP'):
        command = message.content
        tokenFormattedPrice = anyPrice.get_any_price(command, dict_from_csv)
        await message.channel.send(tokenFormattedPrice)

    if message.content.startswith('$deus'):
        deusPrice = deiDeus.get_deus_price()
        await message.channel.send(deusPrice)

    if message.content.startswith('$dei'):
        deiPrice = deiDeus.get_dei_price()
        await message.channel.send(deiPrice)

    if message.content.startswith('$gst'):
        gstPrice = gstGmt.get_gst_price()
        await message.channel.send(gstPrice)

    if message.content.startswith('$gmt'):
        gmtPrice = gstGmt.get_gmt_price()
        await message.channel.send(gmtPrice)

    if message.content.startswith('$colortext'):
        colortextexample = colorTest.color_test()
        await message.channel.send(colortextexample)

    if message.content.startswith('$boo'):
        booPrice = FtmEco.get_boo_price()
        await message.channel.send(booPrice)

    if message.content.startswith('$crv'):
        crvPrice = FtmEco.get_crv_price()
        await message.channel.send(crvPrice)


client.run('')
