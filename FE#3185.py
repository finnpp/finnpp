from http import client
from lib2to3.pgen2 import token
from turtle import color
import discord
import colorama
import time
import random



token = 'OTcxMDQ3ODc2ODQ1MjczMTE4.YnE0zw.Tp79Bb36EyPt4rh9H-TpYF01Gag'

client = discord.Client()



@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.auther).split('#')[0]

client.run(token)


if client.run:
    print("Bot Is Online")
