import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import string
import random

Client = discord.Client()
client = commands.Bot(command_prefix='#')


@client.event
async def on_ready():
    print("Bot connected.")
    print(discord.version_info)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif "hello there" in message.content:
        await client.send_message(message.channel, "GENERAL KENOBI!!!!")
    elif "men" in message.content:
        i = 0
        mystring = message.content
        parts = mystring.split(' ')
        while(i < 50):
            if "men" in parts[i]:
                parts1 = parts[i].replace("men", "women")
                parts2 = parts[i].replace("men", "children")
                fullstring = "Not only the " + parts[i] + " but also the " + parts1 + " and " + parts2 + " too."
                await client.send_message(message.channel, fullstring)
                break
            else:
                i=i+1
    elif "good bot" in message.content:
        await client.send_message(message.channel, "I think YOU'RE a good bot!")
client.run("BOT_TOKEN_HERE")
