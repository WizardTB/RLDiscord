import discord
import asyncio
import http.client
import requests
from bs4 import beautifulsoup
from lxml import html
import time
import sys
import random
import urllib3
import re

urllib3.disable_warnings()

page = requests.get('https://rl.insider.gg/pc')
print(page)


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')
    await client.change_presence(game=discord.Game(name='!help'))

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, 'Working.')
    if message.content.startswith('!as'):
        await client.send_message(message.channel, ':arrows_counterclockwise: Checking prices...')
        content_price = []
        for x in range(0, len(message.content)):
            content_price.append(message.context[x])
            print(content_price)
    if message.content.startswith('!price'):
        new_message = []
        for x in range(0, len(message.content)):
            new_message.append(message.content[x])
        for o in range(0, 7):
            new_message.remove(new_message[0])
        message_final = ''
        for z in range(0, len(new_message)):
            message_final += new_message[z]
            message_finala = '**:arrows_counterclockwise: Checking prices for: ' + '`'+ message_final +'`**'
        await client.send_message(message.channel, message_finala)
        url = 'https://rl.insider.gg/pc/' + message_final
        await client.send_message(message.channel, url)
        ourUrl = opener.open(url).read()
        soup = BeautifulSoup(ourUrl)
        body = soup.find(text=message_final).findnext('h1')
        print(body)
client.run('MzczNjYzMjE3OTQ1MjgwNTEy.DN63iA.USaOXi2RmiNAJPCufYjy8NtACpg')