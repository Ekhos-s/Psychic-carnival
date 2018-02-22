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
    elif "darth" in message.content:
        await client.send_message(message.channel, "Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
    elif "senate" in message.content:
        await client.send_message(message.channel, "I AM THE SENATE")
    elif message.content == "Tell me a joke.":
        await client.send_message(message.channel, "The rank of master.")
    elif "?" in message.content:
        await client.send_message(message.channel, "What about the droid attack on the wookies?")
    elif "do it" in message.content or "Do it" in message.content:
        await client.send_message(message.channel, "dewit!")
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
client.run("NDE1NjcwMzk5MjY3NzY2Mjgz.DW969g.jUv7IJ5m1rH2c2ZUzmNTFKPxmvk")
